#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kafka


producer = kafka.producer.Producer('test')

with producer.batch() as messages:
    print 'Batching a send of multiple messages...'
    messages.append(kafka.message.Message("first message to send"))
    messages.append(kafka.message.Message("second message to send"))
