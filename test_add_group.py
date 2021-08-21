# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


def open_home_page(wd):
    wd.get("http://localhost/addressbook/")


def login(wd):
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys("admin")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys("secret")
    wd.find_element_by_xpath("//input[@value='Login']").click()


def open_groups_page(wd):
    wd.find_element_by_link_text("groups").click()


def create_group(wd):
    # init group creation
    wd.find_element_by_name("new").click()
    # fill group form
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys("test group")
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys("leader")
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys("footer")
    # submit group creation
    wd.find_element_by_name("submit").click()


def return_to_groups_page(wd):
    wd.find_element_by_link_text("group page").click()


def logout(wd):
    wd.find_element_by_link_text("Logout").click()


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        open_home_page(wd)
        login(wd)
        open_groups_page(wd)
        create_group(wd)
        return_to_groups_page(wd)
        logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
