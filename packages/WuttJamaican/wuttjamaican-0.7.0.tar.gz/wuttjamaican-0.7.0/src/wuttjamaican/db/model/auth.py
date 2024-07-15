# -*- coding: utf-8; -*-
################################################################################
#
#  WuttJamaican -- Base package for Wutta Framework
#  Copyright © 2023-2024 Lance Edgar
#
#  This file is part of Wutta Framework.
#
#  Wutta Framework is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option) any
#  later version.
#
#  Wutta Framework is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  Wutta Framework.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Auth Models

The :term:`auth handler` is primarily responsible for managing the
data for these models.

Basic design/structure is as follows:

* :class:`User` may be assigned to multiple roles
* :class:`Role` may contain multiple users (cf. :class:`UserRole`)
* :class:`Role` may be granted multiple permissions
* :class:`Permission` is a permission granted to a role
* roles are not nested/grouped; each is independent
* a few roles are built-in, e.g. Administrators

So a user's permissions are "inherited" from the role(s) to which they
belong.
"""

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.associationproxy import association_proxy

from .base import Base, uuid_column, uuid_fk_column


class Role(Base):
    """
    Represents an authentication role within the system; used for
    permission management.

    .. attribute:: permissions

       List of keys (string names) for permissions granted to this
       role.

       See also :attr:`permission_refs`.

    .. attribute:: users

       List of :class:`User` instances belonging to this role.

       See also :attr:`user_refs`.
    """
    __tablename__ = 'role'
    __table_args__ = (
        sa.UniqueConstraint('name',
                            # TODO
                            # name='role_uq_name',
                            ),
    )

    uuid = uuid_column()

    name = sa.Column(sa.String(length=100), nullable=False, doc="""
    Name for the role.  Each role must have a name, which must be
    unique.
    """)

    notes = sa.Column(sa.Text(), nullable=True, doc="""
    Arbitrary notes for the role.
    """)

    permission_refs = orm.relationship(
        'Permission',
        back_populates='role',
        doc="""
        List of :class:`Permission` references for the role.

        See also :attr:`permissions`.
        """)

    permissions = association_proxy(
        'permission_refs', 'permission',
        creator=lambda p: Permission(permission=p),
        # TODO
        # getset_factory=getset_factory,
    )

    user_refs = orm.relationship(
        'UserRole',
        # TODO
        # cascade='all, delete-orphan',
        # cascade_backrefs=False,
        back_populates='role',
        doc="""
        List of :class:`UserRole` instances belonging to the role.

        See also :attr:`users`.
        """)

    users = association_proxy(
        'user_refs', 'user',
        creator=lambda u: UserRole(user=u),
        # TODO
        # getset_factory=getset_factory,
    )

    def __str__(self):
        return self.name or ""


class Permission(Base):
    """
    Represents a permission granted to a role.
    """
    __tablename__ = 'permission'
    __table_args__ = (
        sa.ForeignKeyConstraint(['role_uuid'], ['role.uuid'],
                                # TODO
                                # name='permission_fk_role',
                                ),
    )

    role_uuid = uuid_fk_column(primary_key=True, nullable=False)
    role = orm.relationship(
        Role,
        back_populates='permission_refs',
        doc="""
        Reference to the :class:`Role` for which the permission is
        granted.
        """)

    permission = sa.Column(sa.String(length=254), primary_key=True, doc="""
    Key (name) of the permission which is granted.
    """)

    def __str__(self):
        return self.permission or ""


class User(Base):
    """
    Represents a user of the system.

    This may or may not correspond to a real person, i.e. some users
    may exist solely for automated tasks.
    """
    __tablename__ = 'user'
    __table_args__ = (
        sa.UniqueConstraint('username',
                            # TODO
                            # name='user_uq_username',
                            ),
    )

    uuid = uuid_column()

    username = sa.Column(sa.String(length=25), nullable=False, doc="""
    Account username.  This is required and must be unique.
    """)

    password = sa.Column(sa.String(length=60), nullable=True, doc="""
    Hashed password for login.  (The raw password is not stored.)
    """)

    active = sa.Column(sa.Boolean(), nullable=False, default=True, doc="""
    Flag indicating whether the user account is "active" - it is
    ``True`` by default.

    The default auth logic will prevent login for "inactive" user accounts.
    """)

    role_refs = orm.relationship(
        'UserRole',
        back_populates='user',
        doc="""
        List of :class:`UserRole` records.
        """)

    def __str__(self):
        return self.username or ""


class UserRole(Base):
    """
    Represents the association between a user and a role.
    """
    __tablename__ = 'user_x_role'
    __table_args__ = (
        sa.ForeignKeyConstraint(['user_uuid'], ['user.uuid'],
                                # TODO
                                # name='user_x_role_fk_user',
                                ),
        sa.ForeignKeyConstraint(['role_uuid'], ['role.uuid'],
                                # TODO
                                # name='user_x_role_fk_role',
                                ),
    )

    uuid = uuid_column()

    user_uuid = uuid_fk_column(nullable=False)
    user = orm.relationship(
        User,
        back_populates='role_refs',
        doc="""
        Reference to the :class:`User` involved.
        """)

    role_uuid = uuid_fk_column(nullable=False)
    role = orm.relationship(
        Role,
        back_populates='user_refs',
        doc="""
        Reference to the :class:`Role` involved.
        """)
