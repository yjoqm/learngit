#!/usr/bin/env python
# coding=utf-8

from flask.ext.principal import RoleNeed, Permission

admin = Permission(RoleNeed('admin'))
common = Permission(RoleNeed('common'))
