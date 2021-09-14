from model.contact import Contact
from model.group import Group


def test_add_new_contact(app):
    contact = Contact(firstname="Firstname", lastname="Lastname")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)


#def test_add_new_empty_contact(app):
#    contact = Contact(firstname=" ")
#   old_contacts = app.contact.get_contact_list()
#    app.contact.create(contact)
#   new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
