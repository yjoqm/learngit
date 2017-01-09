from kombu.pools import producers
import time
from kombu import Exchange, Queue
import json
import uuid
from kombu import Connection
import copy
import random
import string
import requests

class RequestMQ:
    def set_vddb_serv(self,user,pwd,host,port):
        URL='amqp://%s:%s@%s:%s//'%(user,pwd,host,port)
        self.connection = Connection(URL)

    def random_str(self,num):
        '''
         return random string include:[a-z][0-9].
         num: the string length.

        '''
        return string.join(random.sample(['a','b','c','d','e','f','g',\
        'h','i','j','k','l','m','n','o','p','q','r','s','t',\
        'u','v','w','x','y','z',\
        '0','1','2','3','4','5','6','7','8','9'], num)).replace(" ","")

    def send_one_MQMsg(self,file_type,external_id,site_asset_id,\
        extra_info,parent_info=None,extra_info_url=None):
        '''
        1.set vddb serv
        2.sendOneMsgToVddb
        EXAMPLE:
         "site_asset_id": [
                     "url_hash#1asdf12312safd12",
                     "file_hash#123456567"
                 ]
        \n
        file_type:both_2/both_1/both_0/audio_2/audio_1/audio_0/video_2/video_1/video_0
        \n
        'extra_info': {
            'url_hash': 'url_hash#ljtest_dkvx7n82cjfm5bhtipsorze46q130u9layw',
            'url': 'http: //182.92.11.67:88/sample/testfil2.tar',
            'client_id': '123',
            'thunder_hash': '',
            'file_path': './Shayne.f4v',
            'digest': 'ljtest_dkvx7n82cjfm5bhtipsorze46q130u9layw',
            'seed_hash': ''
            }
         p'parent_info': [{u'url_hash#ljtest_dkvx7n82cjfm5bhtipsorze46q130u9layw': 2}]

        "extra_info_url": "2014-08-21_09/tmp/downloader\
        /tmp/2014-08-21/9cc3597c-28d4-11e4-80c4-00163e001022/9ccbf73a-28d4-11e4-80c4-00163e001022.casd"
        '''
        temple_data= {
            "jsonrpc": "2.0",
            "method" : "query",
            "params": {
            'extra_info': {
                'url_hash': 'url_hash#ljtest_dkvx7n82cjfm5bhtipsorze46q130u9layw',
                'url': 'http: //182.92.11.67:88/sample/testfil2.tar',
                'client_id': '123',
                'thunder_hash': '',
                'file_path': './Shayne.f4v',
                'digest': 'ljtest_dkvx7n82cjfm5bhtipsorze46q130u9layw',
                'seed_hash': ''
                },
                 "extra_info_url": "",
                 "files":
                 "2014-08-04_13/cappella.merged.dna",
                 "site_asset_id": [
                     "url_hash#1asdf12312safd12",
                     "file_hash#123456567"
                 ],
                 "priority": 0,
                 "company": 2,
                 "profile": "default",
                 "query_scope": [],
                 'parent_info': [],
                 "external_id":"1234"
                 },
                 "id": 1
        }

        #task_id
        temple_data["params"]["external_id"]=external_id

        #parent_info
        if parent_info !=None:
            temple_data["params"]["parent_info"]=parent_info
        
        #extra_info
        temple_data["params"]["extra_info"]=extra_info

        #extra_info_url
        if extra_info_url!=None:
            temple_data["params"]["extra_info_url"]="2014-08-21_09/tmp/downloader/tmp/2014-08-21/9cc3597c-28d4-11e4-80c4-00163e001022/-%s.casd"%(self.random_str(7))

        #site_asset_id
        temple_data["params"]["site_asset_id"]=site_asset_id

        k=file_type
        if k=="both_2":
            temple_data["params"]["files"]="2014-08-04_13/cappella.merged.dna"
        elif k=="both_1":
            temple_data["params"]["files"]="2014-08-04_13/cappella.merged.dna"
        elif k=="both_0":
            temple_data["params"]["files"]="2014-08-04_13/kexbsn.flv.far.dna"
        elif k=="audio_2":
            temple_data["params"]["files"]="2014-08-04_13/cappella_1.1.flv.1.adna"
        elif k=="audio_1":
            temple_data["params"]["files"]="2014-08-04_13/Wish_You_Were_Here.1.adna"
        elif k=="audio_0":
            temple_data["params"]["files"]="2014-08-04_13/kexbsn.flv.far.dna.1.adna"
        elif k=="video_2" or k=="video_1":
            temple_data["params"]["files"]="2014-08-04_13/cappella_1.1.flv.0.dna"
        elif k=="video_0":
            temple_data["params"]["files"]="2014-08-04_13/kexbsn.flv.far.dna.0.dna"
        else:
            temple_data["params"]["files"]="2014-08-04_13/kexbsn.flv.far.dna"


        message = json.dumps(temple_data)
        #print message

        task_exchange = Exchange('query_queue')
        with producers[self.connection].acquire(block=True) as producer: \
                producer.publish(message,serializer='json',compression='zlib',\
                    exchange=task_exchange,declare=[task_exchange],routing_key='query_queue')
        return message

    def set_result_management(self,ssl,host,port):
        self.rm_ssl=ssl
        self.rm_host=host
        self.rm_port=port

    def http_result_management(self,params):
        '''
         EXAMPLE:\n
         http://host:port/vddb-async/matches?\n
         site_asset_id=url_hash#f8fabdde-e0f4-11e3-b471-fa163e4c5cc4&all_matches=True

         params={
         'site_asset_id':url_hash#xxxxx,
         'all_matches':True,               
         }
        '''
        URL = '{}://{}:{}/vddb-async/matches'.format(self.rm_ssl, self.rm_host, self.rm_port)

        print "request:url:\n%s\nparams:\n%s\n"%(URL,params)
        resp = requests.get(URL, headers={}, params=params, verify=False)  

        return [resp.status_code,resp.text]