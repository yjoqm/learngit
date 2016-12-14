#!/usr/bin/env python
# coding=utf-8

import os
from sona.conf.env import sona_db_uri
base_dir = os.path.dirname(os.path.abspath(__file__))

class DefaultConfig(object):
    DEBUG = True
    LOG_LEVEL = "INFO"
    SECRET_KEY = "seraph"
    TEMPLATE_FOLDER = os.path.join(base_dir,'templates')
    STATIC_FOLDER = os.path.join(base_dir,'static')
    LOGIN_VIEW = 'accounts.login_handler'
    LOG_PATH = '/tmp/sona'


class DevConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = sona_db_uri

class ProductionConfig(DefaultConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = sona_db_uri


if __name__ == '__main__':
    c = DefaultConfig()
    print c.LOGIN_VIEW
