from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Edit contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(
        Contact(firstname="Edit contact", middlename="Edit contact", lastname="Edit contact", nickname="Edit contact",
                title="123", company="123", address="123", address_1="132",
                home_phone="123", mobile_phone="123", work_phone="123", fax="123", email="123", email_2="123",
                email_3="132", homepage="132",
                b_day="1", b_month="May", b_year="2000", ann_day="2", ann_month="May", ann_year="2000", phone2="123",
                notes="123"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)