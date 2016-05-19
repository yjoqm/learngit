#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kafka


producer = kafka.producer.Producer('segment_log')
message1 = kafka.message.Message('Foo!')
message2 = kafka.message.Message('Bar!')
producer.send([message1, message2])
