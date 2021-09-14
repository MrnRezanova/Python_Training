from model.contact import Contact
from model.group import Group


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Editcontact", lastname="Editcontact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Editcontact", lastname="Editcontact")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
