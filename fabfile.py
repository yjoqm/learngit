#!/usr/bin/env python
# coding=utf-8
from fabric.api import * 
from datetime import datetime

'''
def exists(path):
    with lcd(path):
        return local(' ls -l %s'% path)
        print "env user:"% env.user
'''

env.user = 'ellen'
env.hosts = ['192.168.0.229']
env.password = 'ellen123'

def pack():
    '定义一个打包的任务'
    local_path = '/Users/admin/work/UC/uc_pbfile'
    with lcd(local_path):
        #local('tar -czvf testfab.tar.gz --exclude=\'*.tar.gz\' --exclude=\'fabfile.py\' %s' % ' '.join(tar_file))
        local('tar -zcvf testfab.tar.gz test.py')
        local('ls .')
def setting_local():
    local('echo some things~')

def deploy():
    setting_local()
    pack()
    '定义一个部署任务'
    #远程服务器的临时文件
    print "remote env..." 
    with cd('/home/ellen/conf'):
        put('{}/testfab.tar.gz'.format(local_path),'.')
        run('tar -xzvf testfab.tar.gz')
        run('ls .')
    #remote_tmp_tar = '/tmp/testfab.tar.gz'
   # tag = datetime.now().strftime('%y.%m.%d_%H.%M.%S')
    #run('rm -f %s' % remote_tmp_tar)
    #上 传TAR 文件到远程服务器
   # put('testfab.tar.gz',remote_tmp_tar)
  #  
  #  remote_dist_dir = '/home/ellen/test_fab%s' % tag
   # remot_dist_link = '/home/ellen/'
   # run('mkdir %s' % remote_dist_dir)
   # with cd(remote_dist_dir):
   #     run('tar -xzvf %s' %remote_tmp_tar)
   #     run('ls -l')

    # 设定新目录的www-data权限:
    # run('chown -R www-data:www-data %s' % remote_dist_dir)

