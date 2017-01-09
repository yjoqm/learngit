#!/usr/bin/env python
# coding=utf-8

'''
验证库是否有重复的用户
用户名保存在db中,输入的用户名比较db，如有相同则提示,退出程序 
'''
db = {'a':123,'b':345}


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
print 'db:', db

if __name__ == '__main__':
    t = newuser()
    print t 
