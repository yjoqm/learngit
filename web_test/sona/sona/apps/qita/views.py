#!/usr/bin/env python
# coding=utf-8

from flask import (Flask, g, render_template, abort, request, Blueprint, url_for, make_response)
from flask.ext.login import login_required
from sona.apps import logger

qita = Blueprint('qita', __name__)

import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dbase_setup import Base, Notes
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///notepad.db')
Session = sessionmaker(bind=engine)
DBsession = Session()

# configuration
DATABASE = './notepad.db'
app = Flask(__name__)
USERNAME = 'user'
PASSWORD = 'user'
SECRET_KEY = '\x83\xc0\x08\xcd\xe3\x12\xa8'

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@qita.route('/', methods=['POST','GET'])
@login_required
def index_handler():
    #return render_template('accounts/success.html')
    return render_template('notes/editedNote.html')
