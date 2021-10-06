from test.test_phones import merge_phones_like_on_home_page
from model.group import Group


def test_all_entry_field_contact_on_edit_page(app, db):
    old_contacts = db.get_contact_list()
    contact_from_home_page = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(contact_from_home_page, key=Group.id_or_max)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email_2, contact.email_3])))