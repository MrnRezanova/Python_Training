from model.contact import Contact
from model.group import Group
import random


def test_edit_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Editcontact", lastname="Editcontact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    edit_contact = Contact(firstname="Editcontact", lastname="Editcontact")
    edit_contact.id = contact.id
    app.contact.edit_contact_by_id(contact.id, edit_contact)
    # assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact)] = edit_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)
