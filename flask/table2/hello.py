#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template,session, redirect, url_for,flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('what is your name?', validators = [Required()])
    submit = SubmitField('submit')






@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods = ['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name') #session.get 可以拿到get name
        if old_name is not None and old_name != form.name.data:
            flash('looks like you have changed your name!')
        session['name']=form.name.data #局部变量 name 被用于存储用户在表单中输入的名字。这个变量现 在保存在用户会话中,即 session['name']
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))
#每次提交的名字和储存在用户会话中的名字相比较，如果不一样就会调用flash()函数，在发给客户端下一个响应中显示 一个消息
#Flask 把 get_flashed_ messages() 函数开放给模板,用来获取并渲染消息，可以在base.html中添加该函数

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
