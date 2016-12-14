#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from flask.ext.login import UserMixin

from sona.exts import db
from sona.utils.common import get_md5


userbindrole = db.Table('userbindrole',
                        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                        db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
                        )

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email    = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    datatime = db.Column(db.DateTime, default=datetime.now)
    roles    = db.relationship('Role', secondary=userbindrole,
                                       backref=db.backref('users',lazy='dynamic'))

    def __init__(self, username, email, password, roles):
        self.username = username
        self.email    = email
        self.password = get_md5(password)
        self.roles    = roles

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Role(db.Model):

    __tablename__ = 'roles'

    id       = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(80), unique=True)
    datatime = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, rolename):
        self.rolename = rolename

    def __repr__(self):
        return '<Role {}>'.format(self.rolename)


class Notes(db.Model):

    __tablename__ = 'notes'

    id       = db.Column(db.Integer, primary_key=True)
    notename = db.Column(db.String(80), unique=True)
    datatime = db.Column(db.DateTime, default=datetime.now)
    notecontent = db.Column(db.Text) 
    def __init__(self, rolename):
        self.rolename = rolename
