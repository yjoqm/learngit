#!/usr/bin/env python
# coding=utf-8
import requests
s = requests.Session()
test_s = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
print 's.text is %s' % test_s.text
r = s.get('http://httpbin.org/cookies')
print 'r.text is %s' %r.text




