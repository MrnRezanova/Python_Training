# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from test_add_group import login, open_home_page, logout


def create_contact(wd, contact):
    wd.find_element_by_name("firstname").click()
    wd.find_element_by_name("firstname").clear()
    wd.find_element_by_name("firstname").send_keys(contact.firstname)
    wd.find_element_by_name("middlename").click()
    wd.find_element_by_name("middlename").clear()
    wd.find_element_by_name("middlename").send_keys(contact.middlename)
    wd.find_element_by_name("lastname").click()
    wd.find_element_by_name("lastname").clear()
    wd.find_element_by_name("lastname").send_keys(contact.lastname)
    wd.find_element_by_name("nickname").click()
    wd.find_element_by_name("nickname").clear()
    wd.find_element_by_name("nickname").send_keys(contact.nickname)
    wd.find_element_by_name("title").click()
    wd.find_element_by_name("title").clear()
    wd.find_element_by_name("title").send_keys(contact.title)
    wd.find_element_by_name("company").click()
    wd.find_element_by_name("company").clear()
    wd.find_element_by_name("company").send_keys(contact.company)
    wd.find_element_by_name("address").click()
    wd.find_element_by_name("address").clear()
    wd.find_element_by_name("address").send_keys(contact.address)
    wd.find_element_by_name("home").click()
    wd.find_element_by_name("home").clear()
    wd.find_element_by_name("home").send_keys(contact.home_phone)
    wd.find_element_by_name("mobile").click()
    wd.find_element_by_name("mobile").clear()
    wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
    wd.find_element_by_name("work").click()
    wd.find_element_by_name("work").clear()
    wd.find_element_by_name("work").send_keys(contact.work_phone)
    wd.find_element_by_name("fax").click()
    wd.find_element_by_name("fax").clear()
    wd.find_element_by_name("fax").send_keys(contact.fax)
    wd.find_element_by_name("email").click()
    wd.find_element_by_name("email").clear()
    wd.find_element_by_name("email").send_keys(contact.email)
    wd.find_element_by_name("email2").click()
    wd.find_element_by_name("email2").clear()
    wd.find_element_by_name("email2").send_keys(contact.email_2)
    wd.find_element_by_name("email3").click()
    wd.find_element_by_name("email3").clear()
    wd.find_element_by_name("email3").send_keys(contact.email_3)
    wd.find_element_by_name("homepage").click()
    wd.find_element_by_name("homepage").clear()
    wd.find_element_by_name("homepage").send_keys(contact.homepage)
    wd.find_element_by_name("bday").click()
    Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day)
    wd.find_element_by_name("bmonth").click()
    Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_month)
    wd.find_element_by_name("byear").click()
    wd.find_element_by_name("byear").clear()
    wd.find_element_by_name("byear").send_keys(contact.b_year)
    wd.find_element_by_name("aday").click()
    Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.ann_day)
    wd.find_element_by_name("amonth").click()
    Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.ann_month)
    wd.find_element_by_name("ayear").click()
    wd.find_element_by_name("ayear").clear()
    wd.find_element_by_name("ayear").send_keys(contact.ann_year)
    wd.find_element_by_name("address2").click()
    wd.find_element_by_name("address2").clear()
    wd.find_element_by_name("address2").send_keys(contact.address_1)
    wd.find_element_by_name("phone2").click()
    wd.find_element_by_name("phone2").clear()
    wd.find_element_by_name("phone2").send_keys(contact.phone2)
    wd.find_element_by_name("notes").click()
    wd.find_element_by_name("notes").clear()
    wd.find_element_by_name("notes").send_keys(contact.notes)
    wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


def open_contact_page(wd):
    wd.find_element_by_link_text("add new").click()


def return_to_home_page(wd):
    wd.find_element_by_link_text("home page").click()


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_contact_page(wd)
        create_contact(wd, Contact(firstname="First name", middlename="Middle name", lastname="Last name", nickname="Nickname", title="Title", company="Company", address="Address", address_1="Address", home_phone="Home", mobile_phone="Mobile", work_phone="Work", fax="Fax", email="Email", email_2="Email2", email_3="Email3", homepage="Homepage", b_day="2", b_month="February", b_year="2000", ann_day="5", ann_month="June", ann_year="1900", phone2="Home", notes="Notes"))
        return_to_home_page(wd)
        logout(wd)

    def test_add_new_empty_contact(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        open_contact_page(wd)
        create_contact(wd, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", address_1="", home_phone="", mobile_phone="", work_phone="", fax="", email="", email_2="", email_3="", homepage="", b_day="", b_month="-", b_year="", ann_day="", ann_month="-", ann_year="", phone2="", notes=""))
        return_to_home_page(wd)
        logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
