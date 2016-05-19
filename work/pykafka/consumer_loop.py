#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kafka


consumer = kafka.consumer.Consumer('segment_log')

for message in consumer.loop():
    print message