# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


def open_home_page(wd):
    wd.get("http://localhost/addressbook/")


def login(wd, username, password):
    open_home_page(wd)
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//input[@value='Login']").click()


def open_groups_page(wd):
    wd.find_element_by_link_text("groups").click()


def create_group(wd, group):
    open_groups_page(wd)
    # init group creation
    wd.find_element_by_name("new").click()
    # fill group form
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(group.name)
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(group.header)
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(group.footer)
    # submit group creation
    wd.find_element_by_name("submit").click()
    return_to_groups_page(wd)


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
        login(wd, username="admin", password="secret")
        create_group(wd, Group(name="test group", header="leader", footer="footer"))
        logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        login(wd, username="admin", password="secret")
        create_group(wd, Group(name="", header="", footer=""))
        logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
