# -*- coding: utf-8; -*-
################################################################################
#
#  wuttaweb -- Web App for Wutta Framework
#  Copyright © 2024 Lance Edgar
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
Base Logic for Views
"""


class View:
    """
    Base class for all class-based views.

    Instances of this class (or rather, a subclass) are created by
    Pyramid when processing a request.  They will have the following
    attributes:

    .. attribute:: request

       Reference to the current
       :class:`pyramid:pyramid.request.Request` object.

    .. attribute:: app

       Reference to the :term:`app handler`.

    .. attribute:: config

       Reference to the app :term:`config object`.
    """

    def __init__(self, request, context=None):
        self.request = request
        self.config = self.request.wutta_config
        self.app = self.config.get_app()
