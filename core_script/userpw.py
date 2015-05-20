#!/usr/bin/env python
# coding=utf-8
db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name take,try another'
            continue
        else:
            break
        pwd = raw_input('passwd:')
        db[name]=pwd



