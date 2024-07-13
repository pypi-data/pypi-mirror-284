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
Event Subscribers

It is assumed that most apps will include this module somewhere during
startup.  For instance this happens within
:func:`~wuttaweb.app.main()`::

   pyramid_config.include('wuttaweb.subscribers')

This allows for certain common logic to be available for all apps.

However some custom apps may need to supplement or replace the event
hooks contained here, depending on the circumstance.
"""

import json

from pyramid import threadlocal

from wuttaweb import helpers


def new_request(event):
    """
    Event hook called when processing a new request.

    The hook is auto-registered if this module is "included" by
    Pyramid config object.  Or you can explicitly register it::

       pyramid_config.add_subscriber('wuttaweb.subscribers.new_request',
                                     'pyramid.events.NewRequest')

    This will add some things to the request object:

    .. attribute:: request.wutta_config

       Reference to the app :term:`config object`.

    .. attribute:: request.use_oruga

       Flag indicating whether the frontend should be displayed using
       Vue 3 + Oruga (if ``True``), or else Vue 2 + Buefy (if
       ``False``).
    """
    request = event.request
    config = request.registry.settings['wutta_config']
    app = config.get_app()

    request.wutta_config = config

    def use_oruga(request):
        spec = config.get('wuttaweb.oruga_detector.spec')
        if spec:
            func = app.load_object(spec)
            return func(request)
        return False

    request.set_property(use_oruga, reify=True)


def before_render(event):
    """
    Event hook called just before rendering a template.

    The hook is auto-registered if this module is "included" by
    Pyramid config object.  Or you can explicitly register it::

       pyramid_config.add_subscriber('wuttaweb.subscribers.before_render',
                                     'pyramid.events.BeforeRender')

    This will add some things to the template context dict.  Each of
    these may be used "directly" in a template then, e.g.:

    .. code-block:: mako

       ${app.get_title()}

    Here are the keys added to context dict by this hook:

    .. data:: 'app'

       Reference to the :term:`app handler`.

    .. data:: 'config'

       Reference to the app :term:`config object`.

    .. data:: 'h'

       Reference to the helper module, :mod:`wuttaweb.helpers`.

    .. data:: 'json'

       Reference to the built-in module, :mod:`python:json`.

    .. data:: 'url'

       Reference to the request method,
       :meth:`~pyramid:pyramid.request.Request.route_url()`.
    """
    request = event.get('request') or threadlocal.get_current_request()
    config = request.wutta_config
    app = config.get_app()

    context = event
    context['app'] = app
    context['config'] = config
    context['h'] = helpers
    context['url'] = request.route_url
    context['json'] = json

    # TODO
    context['menus'] = []


def includeme(config):
    config.add_subscriber(new_request, 'pyramid.events.NewRequest')
    config.add_subscriber(before_render, 'pyramid.events.BeforeRender')
