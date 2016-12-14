#!/usr/bin/env python
# coding=utf-8

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

db = SQLAlchemy()
zampda_db = SQLAlchemy()
lm = LoginManager()

