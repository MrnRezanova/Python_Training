# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(
        Contact(firstname="First name", middlename="Middle name", lastname="Last name", nickname="Nickname",
                title="Title", company="Company", address="Address", address_1="Address", home_phone="Home",
                mobile_phone="Mobile", work_phone="Work", fax="Fax", email="Email", email_2="Email2", email_3="Email3",
                homepage="Homepage", b_day="2", b_month="February", b_year="2000", ann_day="5", ann_month="June",
                ann_year="1900", phone2="Home", notes="Notes"))
    app.logout()


def test_add_new_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", address_1="",
                home_phone="", mobile_phone="", work_phone="", fax="", email="", email_2="", email_3="", homepage="",
                b_day="", b_month="-", b_year="", ann_day="", ann_month="-", ann_year="", phone2="", notes=""))
    app.logout()
