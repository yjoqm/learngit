#!/usr/bin/env python
# coding=utf-8

from flask import (g, render_template, abort, request, Blueprint, url_for, make_response)
from flask.ext.login import login_required
from sona.apps import logger
from flask import (Blueprint, request, abort, render_template, redirect, url_for, Response)
flaskr = Blueprint('flaskr', __name__)

@flaskr.route('/', methods=['POST','GET'])
@login_required
def index_handler():
#    return render_template('accounts/success.html')
    return  redirect(url_for('flaskr.first_handler'))



@flaskr.route('/1', methods=['POST','GET'])
@login_required
def first_handler():
    if request.method == 'GET':
        return render_template('flaskr/first.html')
    elif request.method == 'POST':
        return render_template('flaskr/first.html')

@flaskr.route('/2', methods=['POST','GET'])
@login_required
def second_handler():
    if request.method == 'GET':
        return render_template('flaskr/second.html')
    elif request.method == 'POST':
        pass
