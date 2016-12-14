#!/usr/bin/env python
# coding=utf-8

from sona.exts import lm, db
from sona.apps import logger
from sona.apps.accounts.models import User, Role
from flask.ext.login import login_user, logout_user, login_required
from flask.ext.principal import identity_changed, Identity, \
        AnonymousIdentity
from flask import render_template, redirect, session, flash,\
        request, Blueprint, url_for, current_app, abort
from sona.utils.common import get_md5
from sona.apps.accounts.permissons import admin


accounts = Blueprint('accounts',__name__)


@lm.user_loader
def load_user(userid):
    return User.query.filter_by(id=userid).first()

@accounts.route('/login',methods=['POST','GET'])
def login_handler():
    if request.method == "GET":
        return render_template('accounts/login.html')
    elif request.method == "POST":
        form_dict = dict(request.form)
        s_user = User.query.filter_by(username=form_dict['username'][0],\
                password=get_md5(form_dict['password'][0])).first()
        if s_user:
            logger.info('user {} login success'.format(s_user))
            login_user(s_user)
            identity_changed.send(current_app._get_current_object(),
                    identity=Identity(s_user.id))
            flash('success login','success')
            return redirect(url_for('index_handler'))

        flash('login name or password wrong','error')
        return redirect(url_for('accounts.login_handler'))
    else:
        abort(404)



@accounts.route('/logout')
@login_required
def logout_handler():
    logout_user()
    for key in ('identity.name','identity.auth_type'):
        session.pop(key,None)
    identity_changed.send(current_app._get_current_object(),
            identity=AnonymousIdentity())
    return redirect(url_for('accounts.login_handler'))



@accounts.route('/',methods=['GET'])
@admin.require(403)
def show_index_handler():
    return redirect(url_for('accounts.show_user_handler'))

@accounts.route('/users', methods=['POST','GET'])
@admin.require(403)
def show_user_handler():
    if request.method == "GET":
        users = User.query.all()
        return render_template('accounts/users.html',users=users)
    elif request.method == "POST":
        form_dict = dict(request.form)
        role_list = []
        roles = form_dict['roles'][0]
        for role_name in roles.split(','):
            role_list.append(Role.query.filter_by(rolename=role_name).first())
        del form_dict['roles']
        if not role_list:
            flash('role not exist','error')
            return redirect(url_for('accounts.show_user_handler'))
        form_dict = {k:v[0] for k,v in form_dict.iteritems()}
        form_dict['roles'] = role_list
        new_user = User(**form_dict)
        db.session.add(new_user)
        db.session.commit()
        logger.info('add user success :===> {}'.format(new_user))
        flash('create success','success')
        return redirect(url_for('accounts.show_user_handler'))
    else:
        abort(404)


@accounts.route('/users/<int:user_id>',methods=['GET'])
@admin.require(403)
def delete_user_handler(user_id):
    del_user = User.query.filter_by(id=user_id).first()
    db.session.delete(del_user)
    db.session.commit()
    logger.info('del user success :===> {}'.format(del_user))
    flash('delete success','success')
    return redirect(url_for('accounts.show_user_handler'))



@accounts.route('/roles/', methods=['POST','GET'])
@admin.require(403)
def show_role_handler():
    if request.method == "GET":
        roles = Role.query.all()
        return render_template('accounts/roles.html',roles=roles)
    elif request.method == "POST":
        form_dict = dict(request.form)
        new_role = Role(rolename=form_dict['rolename'])
        db.session.add(new_role)
        db.session.commit()
        flash('create success', 'success')
        logger.info('create role success :===> {}'.format(new_role))
        return redirect(url_for('accounts.show_role_handler'))
    else:
        abort(404)


@accounts.route('/roles/<int:role_id>',methods=['GET'])
@admin.require(403)
def delete_role_handler(role_id):
    del_role = Role.query.filter_by(id=role_id).first()
    db.session.delete(del_role)
    db.session.commit()
    logger.info('del role success :===> {}'.format(del_role))
    flash('delete success','success')
    return redirect(url_for('accounts.show_role_handler'))
