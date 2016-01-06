#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import session, redirect, url_for, escape, request
#
#session的使用方法例子
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Login in as %s' % escape(session['username'])
    return 'Yor are not logged in '
@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] == request.form['username']
        return redirect(url_for('index'))
    return '''
    <form action="" method="post">
        <p><input type= text name = username>
        <p> input type =submit value=Login>
    </form>
'''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
    #如果会话中有用户名就删除它

from flask import render_template
@app.errorhandler(404) # 指定 404 错误时的处理页面
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#render_template() 后面的 404 ，这表示页面对就的出错代码是 404 ，即页面不存在。缺省情况下 200 表示一切正常
