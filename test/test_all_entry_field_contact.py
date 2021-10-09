from test.test_phones import merge_phones_like_on_home_page
from model.group import Group


def test_all_entry_field_contact_on_edit_page(app, orm):
    all_contacts_from_db = orm.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    for contact in all_contacts_from_db:
        contact.all_email_from_db = merge_emails_like_on_home_page(contact)
        contact.all_phones_from_db = merge_phones_like_on_home_page(contact)
    for index in range(len(all_contacts_from_db)):
        assert all_contacts_from_db[index].all_email_from_db == contacts_from_home_page[index].all_email_from_homepage
        assert all_contacts_from_db[index].all_phones_from_db == contacts_from_home_page[index].all_phones_from_homepage
        assert all_contacts_from_db[index].address == contacts_from_home_page[index].address
    assert sorted(all_contacts_from_db, key=Group.id_or_max) == sorted(contacts_from_home_page, key=Group.id_or_max)



def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email_2, contact.email_3])))