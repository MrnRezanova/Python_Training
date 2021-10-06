from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


def test_add_contact_to_group(app, check_ui):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = Contact(firstname="Editcontact", lastname="Editcontact")
    groups = db.get_group_list()
    group = random.choice(groups)
    old_contacts_list_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group.name)
    new_contacts_list_in_group = db.get_contacts_in_group(group)
    old_contacts_list_in_group.append(contact)
    assert sorted(old_contacts_list_in_group, key=Group.id_or_max) == sorted(new_contacts_list_in_group, key=Group.id_or_max)
    if check_ui:
        assert sorted(db.get_contacts_in_group(group), key=Group.id_or_max) == sorted(app.contact.get_contact_with_group(group.name), key=Group.id_or_max)

