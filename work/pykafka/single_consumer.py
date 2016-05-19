#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kafka


consumer = kafka.consumer.Consumer('segment_log')
messages = consumer.consume()
