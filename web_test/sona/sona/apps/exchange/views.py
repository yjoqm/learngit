#!/usr/bin/env python
# coding=utf-8

from flask import (g, render_template, abort, request, Blueprint, url_for, make_response)
from flask.ext.login import login_required
from sona.apps import logger

exchange = Blueprint('exchange', __name__)

@exchange.route('/', methods=['POST','GET'])
@login_required
def index_handler():
    return render_template('accounts/success.html')
