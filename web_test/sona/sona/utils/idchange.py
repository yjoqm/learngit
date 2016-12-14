#!/usr/bin/env python
# -*- coding: utf-8 -*-


PROJECT_ID = 23

def gen_48mid(advertiser_id, merchant_id):
    return (advertiser_id << 32) + merchant_id

def l48mid2l32(long_id):
    advertiser_id = long_id >> 32
    merchant_id = long_id - (advertiser_id << 32)
    return advertiser_id, merchant_id

def gen_64id(short_id, project_id=PROJECT_ID):
    """
    normal id >> 64 id
    """
    return (1 << 60) + (project_id << 48) + short_id

def l64id_oid(long_id, project_id = PROJECT_ID):
    """
    64 id >> normal id
    """
    return long_id - (1 << 60) - (project_id << 48 )

def l64id2l48(long_id):
    version = long_id >> 60
    project_id = (long_id >> 48) - (version << 12)
    l48_id = long_id - (1 << 60) - (project_id << 48)
    return version, project_id, l48_id

def gen_64mid(advertiser_id, merchant_id):
    """
    m id >> 64 id
    """
    long48mid = gen_48mid(int(advertiser_id), int(merchant_id))
    return gen_64id(long48mid)

def l64mid2l32(long_id):
    """
    64 id >> m id
    """
    version, project_id, l48_id = l64id2l48(int(long_id))
    advertiser_id, merchant_id = l48mid2l32(l48_id)
    return version, project_id, advertiser_id, merchant_id