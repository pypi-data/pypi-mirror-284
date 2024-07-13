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
Application
"""

import os

from wuttjamaican.conf import make_config

from pyramid.config import Configurator


def make_wutta_config(settings):
    """
    Make a WuttaConfig object from the given settings.

    Note that ``settings`` dict will (typically) correspond to the
    ``[app:main]`` section of your config file.

    Regardless, the ``settings`` must contain a special key/value
    which is needed to identify the location of the config file.
    Assuming the typical scenario then, your config file should have
    an entry like this:

    .. code-block:: ini

       [app:main]
       wutta.config = %(__file__)s

    The ``%(__file__)s`` is auto-replaced with the config file path,
    so ultimately ``settings`` would contain something like (at
    minimum)::

       {'wutta.config': '/path/to/config/file'}

    If this config file path cannot be discovered, an error is raised.
    """
    # initialize config and embed in settings dict, to make
    # available for web requests later
    path = settings.get('wutta.config')
    if not path or not os.path.exists(path):
        raise ValueError("Please set 'wutta.config' in [app:main] "
                         "section of config to the path of your "
                         "config file.  Lame, but necessary.")

    wutta_config = make_config(path)

    settings['wutta_config'] = wutta_config
    return wutta_config


def make_pyramid_config(settings):
    """
    Make and return a Pyramid config object from the given settings.

    The config is initialized with certain features deemed useful for
    all apps.
    """
    pyramid_config = Configurator(settings=settings)

    pyramid_config.include('pyramid_beaker')
    pyramid_config.include('pyramid_mako')

    return pyramid_config


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.

    Typically there is no need to call this function directly, but it
    may be configured as the web app entry point like so:

    .. code-block:: ini

       [app:main]
       use = egg:wuttaweb

    The app returned by this function is quite minimal, so most apps
    will need to define their own ``main()`` function, and use that
    instead.
    """
    settings.setdefault('mako.directories', ['wuttaweb:templates'])

    wutta_config = make_wutta_config(settings)
    pyramid_config = make_pyramid_config(settings)

    pyramid_config.include('wuttaweb.static')
    pyramid_config.include('wuttaweb.subscribers')
    pyramid_config.include('wuttaweb.views')

    return pyramid_config.make_wsgi_app()
