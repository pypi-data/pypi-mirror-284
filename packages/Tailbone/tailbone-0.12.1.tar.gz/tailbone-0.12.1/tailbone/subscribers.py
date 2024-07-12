# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2024 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Event Subscribers
"""

import json
import datetime
import logging
import warnings
from collections import OrderedDict

import rattail

import colander
import deform
from pyramid import threadlocal
from webhelpers2.html import tags

import tailbone
from tailbone import helpers
from tailbone.db import Session
from tailbone.config import csrf_header_name, should_expose_websockets
from tailbone.menus import make_simple_menus
from tailbone.util import (get_available_themes, get_global_search_options,
                           should_use_oruga)


log = logging.getLogger(__name__)


def new_request(event):
    """
    Identify the current user, and cache their current permissions.  Also adds
    the ``rattail_config`` attribute to the request.

    A global Rattail ``config`` should already be present within the Pyramid
    application registry's settings, which would normally be accessed via::
    
       request.registry.settings['rattail_config']

    This function merely "promotes" that config object so that it is more
    directly accessible, a la::

       request.rattail_config

    .. note::
       This of course assumes that a Rattail ``config`` object *has* in fact
       already been placed in the application registry settings.  If this is
       not the case, this function will do nothing.

    Also, attach some goodies to the request object:

    * The currently logged-in user instance (if any), as ``user``.

    * ``is_admin`` flag indicating whether user has the Administrator role.

    * ``is_root`` flag indicating whether user is currently elevated to root.

    * A shortcut method for permission checking, as ``has_perm()``.
    """
    log.debug("new request: %s", event)
    request = event.request
    rattail_config = request.registry.settings.get('rattail_config')
    # TODO: why would this ever be null?
    if rattail_config:
        request.rattail_config = rattail_config
    else:
        log.error("registry has no rattail_config ?!")

    def user(request):
        user = None
        uuid = request.authenticated_userid
        if uuid:
            app = request.rattail_config.get_app()
            model = app.model
            user = Session.get(model.User, uuid)
            if user:
                Session().set_continuum_user(user)
        return user

    request.set_property(user, reify=True)

    # nb. only add oruga check for "classic" web app
    classic = rattail_config.parse_bool(request.registry.settings.get('tailbone.classic'))
    if classic:

        def use_oruga(request):
            return should_use_oruga(request)

        request.set_property(use_oruga, reify=True)

    # assign client IP address to the session, for sake of versioning
    Session().continuum_remote_addr = request.client_addr

    request.is_admin = bool(request.user) and request.user.is_admin()
    request.is_root = request.is_admin and request.session.get('is_root', False)

    # TODO: why would this ever be null?
    if rattail_config:

        app = rattail_config.get_app()
        auth = app.get_auth_handler()
        request.tailbone_cached_permissions = auth.get_permissions(
            Session(), request.user)

        def has_perm(name):
            if name in request.tailbone_cached_permissions:
                return True
            return request.is_root
        request.has_perm = has_perm

        def has_any_perm(*names):
            for name in names:
                if has_perm(name):
                    return True
            return False
        request.has_any_perm = has_any_perm

        def register_component(tagname, classname):
            """
            Register a Vue 3 component, so the base template knows to
            declare it for use within the app (page).
            """
            if not hasattr(request, '_tailbone_registered_components'):
                request._tailbone_registered_components = OrderedDict()

            if tagname in request._tailbone_registered_components:
                log.warning("component with tagname '%s' already registered "
                            "with class '%s' but we are replacing that with "
                            "class '%s'",
                            tagname,
                            request._tailbone_registered_components[tagname],
                            classname)

            request._tailbone_registered_components[tagname] = classname
        request.register_component = register_component


def before_render(event):
    """
    Adds goodies to the global template renderer context.
    """
    log.debug("before_render: %s", event)

    request = event.get('request') or threadlocal.get_current_request()
    rattail_config = request.rattail_config
    app = rattail_config.get_app()

    renderer_globals = event
    renderer_globals['rattail_app'] = app
    renderer_globals['app_title'] = app.get_title()
    renderer_globals['app_version'] = app.get_version()
    renderer_globals['h'] = helpers
    renderer_globals['url'] = request.route_url
    renderer_globals['rattail'] = rattail
    renderer_globals['tailbone'] = tailbone
    renderer_globals['model'] = app.model
    renderer_globals['enum'] = request.rattail_config.get_enum()
    renderer_globals['json'] = json
    renderer_globals['datetime'] = datetime
    renderer_globals['colander'] = colander
    renderer_globals['deform'] = deform
    renderer_globals['csrf_header_name'] = csrf_header_name(request.rattail_config)

    # theme  - we only want do this for classic web app, *not* API
    # TODO: so, clearly we need a better way to distinguish the two
    if 'tailbone.theme' in request.registry.settings:
        renderer_globals['b'] = 'o' if request.use_oruga else 'b' # for buefy
        renderer_globals['theme'] = request.registry.settings['tailbone.theme']
        # note, this is just a global flag; user still needs permission to see picker
        expose_picker = request.rattail_config.getbool('tailbone', 'themes.expose_picker',
                                                       default=False)
        renderer_globals['expose_theme_picker'] = expose_picker
        if expose_picker:

            # TODO: should remove 'falafel' option altogether
            available = get_available_themes(request.rattail_config)

            options = [tags.Option(theme, value=theme) for theme in available]
            renderer_globals['theme_picker_options'] = options

        # heck while we're assuming the classic web app here...
        # (we don't want this to happen for the API either!)
        # TODO: just..awful *shrug*
        # note that we assume "simple" menus nowadays
        if request.rattail_config.getbool('tailbone', 'menus.simple', default=True):
            renderer_globals['menus'] = make_simple_menus(request)

        # TODO: ugh, same deal here
        renderer_globals['messaging_enabled'] = request.rattail_config.getbool(
            'tailbone', 'messaging.enabled', default=False)

        # background color may be set per-request, by some apps
        if hasattr(request, 'background_color') and request.background_color:
            renderer_globals['background_color'] = request.background_color
        else: # otherwise we use the one from config
            renderer_globals['background_color'] = request.rattail_config.get(
                'tailbone', 'background_color')

        # maybe set custom stylesheet
        css = None
        if request.user:
            css = rattail_config.get(f'tailbone.{request.user.uuid}', 'user_css')
            if not css:
                css = rattail_config.get(f'tailbone.{request.user.uuid}', 'buefy_css')
                if css:
                    warnings.warn(f"setting 'tailbone.{request.user.uuid}.buefy_css' should be"
                                  f"changed to 'tailbone.{request.user.uuid}.user_css'",
                                  DeprecationWarning)
        renderer_globals['user_css'] = css

        # add global search data for quick access
        renderer_globals['global_search_data'] = get_global_search_options(request)

        # here we globally declare widths for grid filter pseudo-columns
        widths = request.rattail_config.get('tailbone', 'grids.filters.column_widths')
        if widths:
            widths = widths.split(';')
            if len(widths) < 2:
                widths = None
        if not widths:
            widths = ['15em', '15em']
        renderer_globals['filter_fieldname_width'] = widths[0]
        renderer_globals['filter_verb_width'] = widths[1]

        # declare global support for websockets, or lack thereof
        renderer_globals['expose_websockets'] = should_expose_websockets(rattail_config)


def add_inbox_count(event):
    """
    Adds the current user's inbox message count to the global renderer context.

    Note that this is not enabled by default; to turn it on you must do this:

       config.add_subscriber('tailbone.subscribers.add_inbox_count', 'pyramid.events.BeforeRender')
    """
    request = event.get('request') or threadlocal.get_current_request()
    if request.user:
        renderer_globals = event
        app = request.rattail_config.get_app()
        model = app.model
        enum = request.rattail_config.get_enum()
        renderer_globals['inbox_count'] = Session.query(model.Message)\
                                                 .outerjoin(model.MessageRecipient)\
                                                 .filter(model.MessageRecipient.recipient == Session.merge(request.user))\
                                                 .filter(model.MessageRecipient.status == enum.MESSAGE_STATUS_INBOX)\
                                                 .count()


def context_found(event):
    """
    Attach some more goodies to the request object:

    The following is attached to the request:

    * ``get_referrer()`` function

    * ``get_session_timeout()`` function
    """
    request = event.request

    def get_referrer(default=None, **kwargs):
        if request.params.get('referrer'):
            return request.params['referrer']
        if request.session.get('referrer'):
            return request.session.pop('referrer')
        referrer = request.referrer
        if (not referrer or referrer == request.current_route_url()
            or not referrer.startswith(request.host_url)):
            if default:
                referrer = default
            else:
                referrer = request.route_url('home')
        return referrer
    request.get_referrer = get_referrer

    def get_session_timeout():
        """
        Returns the timeout in effect for the current session
        """
        return request.session.get('_timeout')
    request.get_session_timeout = get_session_timeout


def includeme(config):
    config.add_subscriber(new_request, 'pyramid.events.NewRequest')
    config.add_subscriber(before_render, 'pyramid.events.BeforeRender')
    config.add_subscriber(context_found, 'pyramid.events.ContextFound')
