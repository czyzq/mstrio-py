from mstrio.users_and_groups import User, UserGroup
from mstrio.connection import Connection

from typing import List


def list_security_roles_per_user(connection: "Connection", user_group_name: str = None,
                                 user_group_id: str = None,
                                 include_user_groups: bool = False) -> List[dict]:
    """List security roles for every user in a user group.
    It is possible to provide either name or id of user group.

    Args:
        connection: MicroStrategy connection object returned by
            `connection.Connection()`
        user_group_name (str): name of the user group
        user_group_id (str): id of the user group
        include_user_groups (bool): if True also user groups, which are inside
            provided user group, will be included in the result

    Returns:
        list of dicts where each of them is in given form:
        {
            'type' - type of object (it can be `user` or `user_group`)
            'id' - id of object
            'name' - name of object
            'username' - username of user (for user group it is None)
            'security_roles' - list of security roles which object has
        }
    """

    usrgrp = UserGroup(connection=connection, name=user_group_name, id=user_group_id)
    all_scrt_rls = []
    for member in usrgrp.list_members():
        if not member.get('full_name', None):
            if not include_user_groups:
                continue
            member_type = 'user_group'
            tmp_ug = UserGroup(connection=connection, id=member['id'])
            scrt_rls = tmp_ug.security_roles
        else:
            member_type = 'user'
            tmp_u = User(connection=connection, id=member['id'])
            scrt_rls = tmp_u.security_roles
        m = {
            'type': member_type,
            'id': member['id'],
            'name': member['name'],
            'username': member.get('username', None),
            'security_roles': scrt_rls
        }
        all_scrt_rls.append(m)
    return all_scrt_rls
