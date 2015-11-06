#!/usr/bin/env python
# coding=utf-8
from flask import Blueprint
sample = Blueprint('sample',__name__)

@sample.route('/')
@sample.route('/hello')
def index():
    return "this is a Blueprint page"

