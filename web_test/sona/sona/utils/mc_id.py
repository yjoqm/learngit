#!/usr/bin/env python
# -*- coding: utf-8 -*-

VERSION = 1
PROJECT_ID = 23
CUR_DFS_ID = 2

class Ids(object):
    def __init__(self):
        self.advertiser_id = 0
        self.merchant_id = 0
        self.version = VERSION
        self.dfs_id = CUR_DFS_ID
        self.project_id = PROJECT_ID

    def from_long(self, long_id):
        self.version = long_id >> 60
        long_str = bin(long_id)[2:].zfill(64)
        self.dfs_id = int(long_str[4:8], 2)
        self.project_id = int(long_str[8:16], 2)
        self.advertiser_id = int(long_str[16:32], 2)
        self.merchant_id = int(long_str[32:], 2)
        return "ID: {0} - advertiser id: {1}, merchant id: {2}, version: {3}, dfs id: {4}, project id: {5}".format(
            long_id, self.advertiser_id, self.merchant_id,
            self.version, self.dfs_id, self.project_id)

    def to_long(self, advertiser_id=None, merchant_id=None, version=None, dfs_id=None, project_id=None):
        if advertiser_id is not None:
            self.advertiser_id = int(advertiser_id)
        if merchant_id is not None:
            self.merchant_id = int(merchant_id)
        if version is not None:
            self.version = int(version)
        if dfs_id is not None:
            self.dfs_id = int(dfs_id)
        if project_id is not None:
            self.project_id = int(project_id)
        l_version = self.version << 60
        l_dfs_id = self.dfs_id << 56
        l_project_id = self.project_id << 48
        l_advertiser_id = self.advertiser_id << 32
        return l_version | l_dfs_id | l_project_id | l_advertiser_id | self.merchant_id