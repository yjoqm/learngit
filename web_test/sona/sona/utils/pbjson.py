#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2013, Next Tuesday GmbH
#       Authored by: Seif Lotfy <sfl@nexttuesday.de>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of the FreeBSD Project.
#

import simplejson
from google.protobuf.descriptor import FieldDescriptor as FD
import pdb

global error_description
# global filed_list
# filed_list=[]
error_description=''

class ConvertException(Exception):
    pass

def dict2pb(cls, adict, strict=True):
    """
    Takes a class representing the ProtoBuf Message and fills it with data from
    the dict.
    """
    global error_description
    # global filed_list
    obj = cls()
    # pdb.set_trace()
    try:
        for field in obj.DESCRIPTOR.fields:
            if not field.label == field.LABEL_REQUIRED:
                continue
            if not field.has_default_value:
                continue
            if not field.name in adict:
                error_description='Field "%s" missing from descriptor dictionary.'% field.name
                # print error_description
                raise ConvertException('Field "%s" missing from descriptor dictionary.' % field.name)
        field_names = set([field.name for field in obj.DESCRIPTOR.fields])
        # pdb.set_trace()
        if strict:
            for key in adict.keys():
                if key not in field_names:
                    error_description='Key "%s" can not be mapped to field in %s class.' % (key, type(obj))
                    # print error_description
                    raise ConvertException( 'Key "%s" can not be mapped to field in %s class.'% (key, type(obj)))
        for field in obj.DESCRIPTOR.fields:
                error_description=field.name
                # print error_description

                if not field.name in adict or None == adict[field.name]:
                    continue
                msg_type = field.message_type
                if field.label == FD.LABEL_REPEATED:
                    if field.type == FD.TYPE_MESSAGE:

                        for sub_dict in adict[field.name]:
                            item = getattr(obj, field.name).add()
                            item.CopyFrom(dict2pb(msg_type._concrete_class, sub_dict))
                    else:
                         map(getattr(obj, field.name).append, adict[field.name])
                else:
                    if field.type == FD.TYPE_MESSAGE:
                        value = dict2pb(msg_type._concrete_class, adict[field.name])
                        getattr(obj, field.name).CopyFrom(value)
                    else:
                        if field.type == FD.TYPE_ENUM and type(adict[field.name]) == list and 0 < len(adict[field.name]):
                            adict[field.name] = adict[field.name][0]
                        setattr(obj, field.name, adict[field.name])
    except Exception as ex:
        return 'error '+str(ex)+" "+error_description

    return obj

def pb2dict(obj):
    """
    Takes a ProtoBuf Message obj and convertes it to a dict.
    """
    adict = {}
    # pdb.set_trace()
    if not obj.IsInitialized():
        return None
    for field in obj.DESCRIPTOR.fields:
        if not getattr(obj, field.name):
            continue
        if not field.label == FD.LABEL_REPEATED:
            if not field.type == FD.TYPE_MESSAGE:
                adict[field.name] = getattr(obj, field.name)
            else:
                value = pb2dict(getattr(obj, field.name))
                if value:
                    adict[field.name] = value
        else:
            if field.type == FD.TYPE_MESSAGE:
                adict[field.name] = \
                    [pb2dict(v) for v in getattr(obj, field.name)]
            else:
                adict[field.name] = [v for v in getattr(obj, field.name)]
    return adict


def json2pb(cls, json, strict=True):
    """
    Takes a class representing the Protobuf Message and fills it with data from
    the json string.
    """
    dict_obj=''
    try:
        dict_obj=simplejson.loads(json)
    except:
        return 'error '+':json formate error'
    # pdb.set_trace()
    pb_obj=dict2pb(cls, dict_obj, strict)
    print "pb_obj:"
    print pb_obj
    return pb_obj



def pb2json(obj):
    """
    Takes a ProtoBuf Message obj and convertes it to a json string.
    """
    return simplejson.dumps(pb2dict(obj), sort_keys=True, indent=4)

