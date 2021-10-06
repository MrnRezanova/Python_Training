from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


def test_del_contact_from_group(app, check_ui):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_group_list()) == 0:
        group = Group(name="test")
        app.group.create(group)
        contact = Contact(firstname="contact")
        app.contact.add_contact_to_group(contact, group.name)
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contacts_in_group(group)) == 0:
        contact = Contact(firstname="contact")
        app.contact.add_contact_to_group(contact, group.name)
    contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)
    old_contacts_list_in_group = db.get_contacts_in_group(group)
    old_contacts_list_without_group = db.get_contacts_not_in_group(group)
    app.contact.remove_contact_from_group(contact.id, group.name)
    new_contacts_list_in_group = db.get_contacts_in_group(group)
    new_contacts_list_without_group = db.get_contacts_not_in_group(group)
    old_contacts_list_without_group.append(contact)
    old_contacts_list_in_group.remove(contact)
    assert sorted(old_contacts_list_without_group, key=Group.id_or_max) == sorted(new_contacts_list_without_group, key=Group.id_or_max)
    assert sorted(old_contacts_list_in_group, key=Group.id_or_max) == sorted(new_contacts_list_in_group, key=Group.id_or_max)
    if check_ui:
        assert sorted(db.get_contacts_in_group(group), key=Group.id_or_max) == sorted(app.contact.get_contact_with_group(group.name), key=Group.id_or_max)