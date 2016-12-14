#!/usr/bin/env python
# coding=utf-8
import os
import sys
from sona.utils.common import base_dir
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler



def get_logger(app,path='/var/log/sona',level='INFO',logger_name='sona'):
    if not os.path.exists('/tmp/sona/'):
        os.makedirs('/tmp/sona')

    log_file = os.path.join(path,'app.log')
    formatter = Formatter("[%(asctime)s] [%(pathname)s] [%(name)s] [%(message)s]","%a %d %b %Y %H:%M:%S",)
    time_handler = TimedRotatingFileHandler(log_file,'midnight',1,10)
    time_handler.setFormatter(formatter)

    stream_handler = StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)


    app.logger.addHandler(time_handler)
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(level)
    return app.logger
