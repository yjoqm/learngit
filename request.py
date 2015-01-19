#encoding:utf-8
import requests
'''
r = requests.get("https://github.com/yjoqm/learngit/tree/master",auth=("yjoqm","yjoqm0118"))
print r.status_code
#print r.text
#print r.json()
#print r.encoding
#为url传递参数
payload = {"key1":"value1","key2":"value2"}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url) #print http://httpbin.org/get?key2=value2&key1=value1
'''
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
r = requests.post(url,data=json.dumps(payload),headers=headers)
print r.status_code
#type(data) = str

