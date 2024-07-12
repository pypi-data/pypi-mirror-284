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
WuttJamaican -  base models

.. class:: Base

   This is the base class for all data models.
"""

import sqlalchemy as sa
from sqlalchemy import orm

from wuttjamaican.util import make_uuid


Base = orm.declarative_base()


def uuid_column(*args, **kwargs):
    """
    Returns a UUID column for use as a table's primary key.
    """
    kwargs.setdefault('primary_key', True)
    kwargs.setdefault('nullable', False)
    kwargs.setdefault('default', make_uuid)
    return sa.Column(sa.String(length=32), *args, **kwargs)


class Setting(Base):
    """
    Represents a :term:`config setting`.
    """
    __tablename__ = 'setting'

    name = sa.Column(sa.String(length=255), primary_key=True, nullable=False, doc="""
    Unique name for the setting.
    """)

    value = sa.Column(sa.Text(), nullable=True, doc="""
    String value for the setting.
    """)

    def __str__(self):
        return self.name or ""
