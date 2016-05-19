#!/usr/bin/env python
# coding=utf-8

import sys
import os
import kafka


def send_msg_from_file(file_name):
    if os.path.exists(file_name):
        producer = kafka.producer.Producer('segment_log')

        f = file(file_name)
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print line,

            message = kafka.message.Message(line)
            producer.send(message)

        f.close()
    else:
        print '%s not exists' % file_name


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'please select a file to read'
        exit(1)
    send_msg_from_file(sys.argv[1])
