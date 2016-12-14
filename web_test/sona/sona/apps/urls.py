#!/usr/bin/env python
# coding=utf-8

import json
from flask import (g, request, url_for, redirect)
from flask.ext.login import login_required

from sona.apps import app, logger
from sona.apps.exchange.views import exchange
from sona.apps.accounts.views import accounts
from sona.apps.idhelper.views import idhelper
from sona.apps.qita.views import qita
from sona.apps.flaskr.views import flaskr


app.register_blueprint(exchange, url_prefix='/exchange')
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(idhelper, url_prefix='/idhelper')
app.register_blueprint(qita, url_prefix='/qita')
app.register_blueprint(flaskr, url_prefix='/flaskr')

'''
@app.before_request
def setup_handler():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    method = request.method
    logger.info("{} == {}".format(ip, method))

    platform_list = get_platform_info()
    setattr(g, 'platform_list', platform_list)
    try:
        setattr(g, request.path, json.loads(request.cookies[request.path]))
    except:
        pass

    for platform in platform_list:
        setattr(g, platform, get_input_info(platform))

'''
@login_required
@app.route('/')
def index_handler():
    return redirect(url_for('flaskr.index_handler'))

