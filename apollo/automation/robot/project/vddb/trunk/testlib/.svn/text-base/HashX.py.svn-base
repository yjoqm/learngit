#!/usr/bin/env python
#coding: utf-8
 
import hashlib
import base64
 
class HashX(object):
	"""
	::Reference: http://seals.vobile.cn/trac/vdna/wiki/vobile_thunder/thunder_hash
	 
	Usage:
	======
	>>> print Hash(url="http://www.baidu.com/dl/some.mp4").value
	76709133b1bcd884611186bdefcdbe2e235ef104
	>>> print Hash(url="http://www.baidu.com/dl/some.mp4").protocol
	http
	 
	>>> print Hash(content="TEST_SEED_FILE_CONTENT").value
	fda6c4d1938082c32afea756bdaf1e031349c23a
	>>> print Hash(content="TEST_SEED_FILE_CONTENT").protocol
	torrent
	"""
	 
	def __init__(self, url=None, content=None):
		if url is None and content is None:
			raise ValueError('URL or seed_content required!')
		
		if url:
			self.arg = url
			self.prefix = 'url_hash'
			try:
				self.protocol = url.split('://', 1)[0].lower()
			except Exception as e:
				print e
				raise
		else:
			self.arg = content
			self.prefix = 'seed_hash'
			self.protocol = 'torrent'
			 
		# self.protocol = url.split('://', 1)[0].lower() if url else filename.rsplit('.', 1)[-1].lower()
		# self.prefix = 'url_hash' if url else 'seed_hash'
		self.url = url
		self.content = content
		 
		 
	@property
	def value(self):
		""" Cached property """
		 
		if hasattr(self, '_value'):
			return self._value
		 
		hash_type_dict = {
		'ftp' : HashX.sha1_hex,
		'http' : HashX.sha1_hex,
		'ed2k' : HashX.hash_ed2k,
		'magnet' : HashX.hash_magnet,
		'torrent' : HashX.hash_bt,
		}
		func = hash_type_dict.get(self.protocol.lower(), HashX.sha1_hex)
		self._value = '%s#%s' % (self.prefix, func(self.arg))
		return self._value
	 
	 
	@staticmethod
	def sha1_hex(s):
		if type(s) == unicode:
			s = s.encode('utf-8')
		return hashlib.sha1(s).hexdigest()
	 
	@staticmethod
	def hash_bt(b64_content):
		""" !!! *tmp* !!! """
		return Hash.sha1_hex(b64_content)
	 
	@staticmethod
	def hash_ed2k(uri):
		return uri.split('|')[4]
	 
	@staticmethod
	def hash_thunder(uri):
		uri = uri.strip()
		t_hash = uri[10:-1] if uri.endswith('/') else uri[10:]
		origin_uri = base64.b64decode(t_hash)[2:-2]
		return Hash(url=origin_uri).value
	 
	@staticmethod
	def hash_magnet(uri):
		""" !!! *tmp* !!! """
		return Hash.sha1_hex(uri)
