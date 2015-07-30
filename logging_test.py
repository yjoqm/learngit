#!/usr/bin/env python
# coding=utf-8
import logging
import os


logging.basicConfig(filename = os.path.join(os.getcwd(),'log.txt'),level = logging.DEBUG)
logging.debug('this is a message')
logging.basicConfig(filename = os.path.join(os.getcwd(),'log.txt'), level=logging.WARN,filemod='a',format = '%(asctime)s-%(levelname)s:%(message)s')
logging.debug('debug')
logging.warning('warning')
logging.error('error')


logging.basicConfig(filename = os.path.join(os.getcwd(),'log.txt'), level=logging.DEBUG,format = '%(asctime)s-%(levelname)s:%(message)s')
log = logging.getLogger('thhhhhhest')
log.setLevel(logging.WARN)
log.info('info')
log.debug('debug')
log.warning('warnning')
log.error('error')

#以error级别的日志,异常跟踪信息自动添加到日志消息里.logger.exception通过用在异常处理块中
logging.basicConfig(filename = os.path.join(os.getcwd(),'log.txt'), level=logging.DEBUG,format = '%(asctime)s-%(levelname)s:%(message)s')
log = logging.getLogger('root.test')
try:
    raise Exception, 'this is a Exception'
except:
    log.exception('exception')#异常信息被自动添加到日志消息中


