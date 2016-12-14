#!/usr/bin/env python
# coding=utf-8

from flask.ext.script import Manager, Server, Shell
from sona.apps import app
from sona.exts import db
from sona.apps.accounts.models import User, Role

manager = Manager(app)
server = Server(host='0.0.0.0', port=5002)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', server)

@manager.command
def createdb():
    db.create_all()

@manager.command
def dropdb():
    db.drop_all()

if __name__ == "__main__":
    manager.run()

