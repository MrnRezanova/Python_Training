from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_edit_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("//div[@id='content']/form/input[22]")) > 0 and len(wd.find_elements_by_xpath("//div[@id='content']/form[2]/input[2]")) > 0):
            wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def change_field_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home_phone)
        self.app.change_field_value("mobile", contact.mobile_phone)
        self.app.change_field_value("work", contact.work_phone)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email_2)
        self.app.change_field_value("email3", contact.email_3)
        self.app.change_field_value("homepage", contact.homepage)
        self.change_field_select_value("bday", contact.b_day)
        self.change_field_select_value("bmonth", contact.b_month)
        self.app.change_field_value("byear", contact.b_year)
        self.change_field_select_value("aday", contact.ann_day)
        self.change_field_select_value("amonth", contact.ann_month)
        self.app.change_field_value("ayear", contact.ann_year)
        self.app.change_field_value("address2", contact.address_1)
        self.app.change_field_value("phone2", contact.phone2)
        self.app.change_field_value("notes", contact.homepage)

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_edit_page()
        self.fill_contact_form(contact)
        wd.find_elements_by_xpath("//div[@id='content']/form/input[22]")[index].click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr")[1:]:
                id = element.find_element_by_name("selected[]").get_attribute("value")
                text = element.text
                self.contact_cache.append(Contact(firstname=text.split()[1], lastname=text.split()[0], id=id))
        return list(self.contact_cache)