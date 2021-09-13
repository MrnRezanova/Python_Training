from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(
        Contact(firstname="First name", middlename="Middle name", lastname="Last name", nickname="Nickname",
                title="Title", company="Company", address="Address", address_1="Address", home_phone="Home",
                mobile_phone="Mobile", work_phone="Work", fax="Fax", email="Email", email_2="Email2", email_3="Email3",
                homepage="Homepage", b_day="2", b_month="February", b_year="2000", ann_day="5", ann_month="June",
                ann_year="1900", phone2="Home", notes="Notes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_new_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(
        Contact(firstname=" "))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
