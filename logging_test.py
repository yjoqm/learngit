#!/usr/bin/env python
# coding=utf-8
import logging

'''
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s: %(message)s')
logging.info('ltestset logging message')

#设置自己需要设置的 log后再使用
def initlog():
    logger = logging.getLogger() #生成一个日志对像，可以带一个名字，也可以缺失
    hdlr = logging.FileHandler('yjoqm.log') #生成一个Handler, 支持SocketHandler, SMTPHandler，这里由于写文件就使用了filehandle
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s') #生成一个格式器，规范输出
    hdlr.setFormatter(formatter) #将格式器设置到处理器上
    logger.addHandler(hdlr) #将处理器加到日志对像上
    logger.setLevel(logging.NOTSET) #设置日志信息输出的级别，默认是30warning notset=0，也就是想输出所有信息
    return logger

logger = initlog()
logger.info('message info')
logger.error('message')
#handler：将日志记录（log record）发送到合适的目的地（destination），比如文件，socket等
#一个logger对象可以通过addHandler方法添加0到多个handler，每个handler又可以定义不同日志级别，以实现日志分级过滤显示
#filter：提供一种优雅的方式决定一个日志记录是否发送到Handler
'''


#import logging
import logging.handlers

LOG_FILE = 'yjoqm.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler,文件到达一定大小时拆分
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='midnight', backupCount = 10) # 凌晨时拆分log文件，以免文件太大

fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)#实例化formatter
handler.setFormatter(formatter)#为handler 添加formatter

logger =  logging.getLogger('yjoqm') #获取名为yjoqm的logger
logger.addHandler(handler) #为logger添加Handler
logger.setLevel(logging.DEBUG)

logger.info('first info message')
logger.debug('first debug message')




