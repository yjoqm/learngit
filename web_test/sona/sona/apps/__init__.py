#!/usr/bin/env python
# coding=utf-8

import os
from flask import Flask, render_template
from sona.utils.logger import get_logger
from sona.exts import db
from sona.exts import lm
from flask.ext.principal import identity_loaded, Principal, RoleNeed
from flask.ext.login import current_user


def create_app():
    app = Flask(__name__)
    configure_conf(app)
    configure_identity(app)
    configure_errorhandlers(app)
    configure_template(app)
    configure_static(app)
    configure_exts(app)
    configure_filter(app)
    return app

def configure_exts(app):
    db.init_app(app)
    lm.init_app(app)
    lm.login_view = app.config['LOGIN_VIEW']

def configure_template(app):
    app.template_folder = app.config['TEMPLATE_FOLDER']

def configure_static(app):
    app.static_folder = app.config['STATIC_FOLDER']

def configure_errorhandlers(app):

    if app.debug: return

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error.html',
                error_code=404, error_message='page not found')

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('error.html',
                error_code=403, error_message='forbidden')

    @app.errorhandler(500)
    def server_error(error):
        return render_template('error.html',
                error_code=500, error_message='server error')

    @app.errorhandler(401)
    def unauthorized(error):
        return render_template('error.html',
                error_code=401, error_message='unauthorized')

def configure_filter(app):

    @app.template_filter('decodeutf8')
    def unicode_filter(s):
        if s and isinstance(s,basestring):
            return s.decode('utf-8')
        return s

def configure_identity(app):

    Principal(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user
        if hasattr(current_user,'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.rolename))

def configure_conf(app):
    env = os.getenv('ENV')
    if env in ['dev','debuf','DEV','DEBUG','develop']:
        app.config.from_object('sona.settings.DevConfig')
    else:
        app.config.from_object('sona.settings.ProductionConfig')

app = create_app()
logger = get_logger(app,app.config['LOG_PATH'],app.config['LOG_LEVEL'])

from sona.apps import urls
