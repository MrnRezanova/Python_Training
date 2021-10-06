from model.group import Group
import random


def test_modify_some_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edit_group = Group(name="New")
    edit_group.id = group.id
    app.group.modify_group_by_id(group.id, edit_group)
#    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group)] = edit_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_first_group_header(app):
#    if app.group.count() == 0:
#       app.group.create(Group(name="test"))
#   old_groups = app.group.get_group_list()
#   app.group.modify_first_group(Group(header="New"))
#   new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)
