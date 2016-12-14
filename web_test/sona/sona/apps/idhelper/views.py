#!/usr/bin/env python
# coding=utf-8

from flask.ext.login import login_required
from sona.apps import logger
from sona.utils.mc_id import Ids
from sona.utils.hashcode_translate import getHashCode
from flask import (Blueprint, request, abort, render_template, redirect, url_for, Response)
from sona.utils.idchange import (gen_64id, l64id_oid, gen_64mid, l64mid2l32)
from sona.utils.common import *
import re
import json
import yaml

idhelper = Blueprint('idhelper', __name__)

@idhelper.route('/', methods=['POST','GET'])
@login_required
def index_handler():
    return redirect(url_for('idhelper.n264_handler'))


@idhelper.route('/n264', methods=['POST','GET'])
@login_required
def n264_handler():
    if request.method == 'GET':
        return render_template('idhelper/nidhelper.html')
    elif request.method == 'POST':
        form_dict = dict(request.form)
        oid = form_dict['oid'][0]
        oid=re.sub(";"," ",oid)
        oid=re.sub(":"," ",oid)
        oid=re.sub(","," ",oid)
        oid=re.sub("\s+"," ",oid)
        oid_list=oid.split()
        nids=""
        for id in oid_list:
            if(id!=""):
                n_id=gen_64id(int(id))
                nids=nids+id+":"+str(n_id)+","
        res = {'nid': str(nids)}
        return Response(json.dumps(res), content_type='application/json')
    else:
        abort(404)

@idhelper.route('/hashcode', methods=['POST','GET'])
@login_required
def hashcode_handler():
    if request.method == 'GET':
        return render_template('idhelper/hashcode.html')
    elif request.method == 'POST':
        form_dict = dict(request.form)
        logger.info("from_dict:====> {}".format(form_dict))
        #hashid = int(form_dict['hashid'][0])
        hashid = form_dict['hashid'][0]
        nid = getHashCode(hashid)
        res = {'nid': str(nid)}
        return Response(json.dumps(res), content_type='application/json')
    else:
        abort(404)



@idhelper.route('/642n', methods=['POST','GET'])
@login_required
def six42n_handler():
    if request.method == 'GET':
        return render_template('idhelper/nidhelper.html')
    elif request.method == 'POST':
        form_dict = dict(request.form)
        oid = (form_dict['oid'][0])
        oid=re.sub(";"," ",oid)
        oid=re.sub(":"," ",oid)
        oid=re.sub(","," ",oid)
        oid=re.sub("\s+"," ",oid)
        oid_list=oid.split()
        nids=""
        for id in oid_list:
            if(id!=""):
                n_id=l64id_oid(int(id))
                nids=nids+id+":"+str(n_id)+","
        res = {'nid': str(nids)}
        return Response(json.dumps(res), content_type='application/json')
    else:
        abort(404)

@idhelper.route('/midencode', methods=['POST','GET'])
@login_required
def midencode_handler():
    if request.method == 'GET':
        return render_template('idhelper/midhelper.html')
    elif request.method == 'POST':
        form_dict = dict(request.form)
        form_dict = { k:v[0] for k,v in form_dict.iteritems() }

        mcid = Ids()
        nid = mcid.to_long(form_dict['advertiser_id'],
            form_dict['merchant_id'], form_dict['version'],
            form_dict['dfs_id'], form_dict['project_id'])

        res = {'nid': str(nid)}
        return Response(json.dumps(res), content_type='application/json')
    else:
        abort(404)

@idhelper.route('/middecode', methods=['POST','GET'])
@login_required
def middecode_handler():
    if request.method == 'GET':
        return render_template('idhelper/rmidhelper.html')
    elif request.method == 'POST':
        form_dict = dict(request.form)
        form_dict = { k:v[0] for k,v in form_dict.iteritems() }

        # version, project_id, advertiser_id, merchant_id = l64mid2l32(**form_dict)
        mcid = Ids()
        mcid.from_long(long(form_dict['long_id']))

        advertiser_id = mcid.advertiser_id
        merchant_id = mcid.merchant_id
        version = mcid.version
        dfs_id = mcid.dfs_id
        project_id = mcid.project_id

        info = {
                'advertiser_id':str(advertiser_id),
                'merchant_id':str(merchant_id),
                'version':str(version),
                'dfs_id':str(dfs_id),
                'project_id':str(project_id),
                }
        return render_template('ajax/ajax_id.html', info=info)
    else:
        abort(404)

@idhelper.route('/json2yaml',methods=['GET','POST'])
@login_required
def jsontoyaml():
    if request.method == 'GET':
        return render_template('idhelper/json2yaml.html')
    elif request.method == 'POST':
        form_dict=dict(request.form)
        json_data=form_dict['json_data'][0]
        if json_data:
            yaml_format=json2yaml(json_data)
        else:
            yaml_format="请输入正确的json格式"
        return render_template('idhelper/json2yaml.html',yaml_format=yaml_format)
    else:
        abort(404)

@idhelper.route('/yaml2json',methods=['GET','POST'])
@login_required
def yamltojson():
    if request.method == 'GET':
        return render_template('idhelper/yaml2json.html')
    elif request.method == 'POST':
        form_dict=dict(request.form)
        yaml_data=form_dict['yaml_data'][0]
        if yaml_data:
            json_format=yaml2json(yaml_data)
        else:
            json_format="请输入点东西吧"
        return render_template('idhelper/yaml2json.html',json_format=json_format)
    else:
        abort(404)
