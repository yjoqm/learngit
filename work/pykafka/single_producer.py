#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kafka


producer = kafka.producer.Producer('segment_log')
message = kafka.message.Message('Foo!')
producer.send(message)
