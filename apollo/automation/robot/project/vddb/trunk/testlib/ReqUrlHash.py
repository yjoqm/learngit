#!/usr/bin/env python
#coding: utf-8
 
from HashX import HashX
 
class ReqUrlHash:
	def getHash(self,urlx):
		hash_value=HashX(url=urlx).value
		return hash_value


if '__name__' == '__main__':
	x=ReqUrlHash()
	print x.getHash("XXXXxx");
