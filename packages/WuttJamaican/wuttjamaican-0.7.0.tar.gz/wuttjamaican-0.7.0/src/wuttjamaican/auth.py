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
Auth Handler

This defines the default :term:`auth handler`.
"""

from wuttjamaican.app import GenericHandler


class AuthHandler(GenericHandler):
    """
    Base class and default implementation for the :term:`auth
    handler`.

    This is responsible for "authentication and authorization" - for
    instance:

    * create new users, roles
    * grant/revoke role permissions
    * determine which permissions a user has
    * identify user from login credentials
    """
