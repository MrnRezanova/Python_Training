from test.test_phones import merge_phones_like_on_home_page
from model.group import Group


def test_all_entry_field_contact_on_edit_page(app, orm):
    all_contacts_from_db = orm.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    for contact in all_contacts_from_db:
        contact.all_email_from_homepage = merge_emails_like_on_home_page(contact)
        contact.all_phones_from_homepage = merge_phones_like_on_home_page(contact)
        for contact_from_homepage in contacts_from_home_page:
            if contact.id == contact_from_homepage.id:
                assert contact.address == contact_from_homepage.address
                assert contact.all_email_from_homepage == contact_from_homepage.all_email_from_homepage
                assert contact.all_phones_from_homepage == contact_from_homepage.all_phones_from_homepage
    assert sorted(all_contacts_from_db, key=Group.id_or_max) == sorted(contacts_from_home_page, key=Group.id_or_max)



def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email_2, contact.email_3])))