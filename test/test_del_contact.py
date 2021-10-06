import time
from model.contact import Contact
from model.group import Group
import random


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Edit contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
#    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    time.sleep(2)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)
