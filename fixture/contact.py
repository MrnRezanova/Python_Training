from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(
                wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_edit_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        if not (len(wd.find_elements_by_xpath("//div[@id='content']/form/input[22]")) > 0 and len(
                wd.find_elements_by_xpath("//div[@id='content']/form[2]/input[2]")) > 0):
            wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_edit_page_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        if not (len(wd.find_elements_by_xpath("//div[@id='content']/form/input[22]")) > 0 and len(
                wd.find_elements_by_xpath("//div[@id='content']/form[2]/input[2]")) > 0):
            wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def open_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

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
        self.open_edit_page_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_edit_page_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count_contact_in_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text("[none]")
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr")[1:]:
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_homepage=all_phones,
                                                  all_email_from_homepage=all_email))
        return list(self.contact_cache)

    def get_contact_list_without_group(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            Select(wd.find_element_by_name("group")).select_by_visible_text("[all]")
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr")[1:]:
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_homepage=all_phones,
                                                  all_email_from_homepage=all_email))
        return list(self.contact_cache)

    def get_contact_with_group(self, group):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            wd.find_element_by_name("group").click()
            Select(wd.find_element_by_name("group")).select_by_visible_text("%s" % group)
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr")[1:]:
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_homepage=all_phones,
                                                  all_email_from_homepage=all_email))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_page_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        b_day = wd.find_element_by_name("bday").get_attribute("value")
        b_month = wd.find_element_by_name("bmonth").get_attribute("value")
        b_year = wd.find_element_by_name("byear").get_attribute("value")
        ann_day = wd.find_element_by_name("aday").get_attribute("value")
        ann_month = wd.find_element_by_name("amonth").get_attribute("value")
        ann_year = wd.find_element_by_name("ayear").get_attribute("value")
        notes = wd.find_element_by_name("notes").get_attribute("value")
        address_1 = wd.find_element_by_name("address2").get_attribute("value")
        return Contact(firstname=firstname, id=id, middlename=middlename, lastname=lastname, home_phone=homephone,
                       work_phone=workphone, mobile_phone=mobilephone, phone2=phone2, nickname=nickname,
                       company=company,
                       title=title, address=address, fax=fax, email=email, email_2=email_2, email_3=email_3,
                       homepage=homepage,
                       b_year=b_year, b_day=b_day, b_month=b_month, ann_day=ann_day, ann_year=ann_year,
                       ann_month=ann_month,
                       notes=notes, address_1=address_1)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=homephone, work_phone=workphone,
                       mobile_phone=mobilephone, phone2=phone2)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("%s" % group)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def remove_contact_from_group(self, id, group):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_visible_text("%s" % group)
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//input[@name='remove']").click()
        self.open_contact_page()
