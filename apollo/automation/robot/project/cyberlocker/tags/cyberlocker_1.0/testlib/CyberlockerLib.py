import sys
import os
import json
import requests
from amqplib import client_0_8 as amqp
class CyberlockerLib(object) :
        
    def Assert_True(self,flag):
        assert flag
        
    def Assert_False(self,flag):
        assert not flag
        
    def Assert_Not_Null(self,result):
        assert(result)
    
    def Assert_Null(self,result):
        assert not (result)

    def post_json_data(self,post_url,data_json) :
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        json_response = requests.get(post_url, data=data_json, headers=headers)
        return json_response.content
     
    def check_request_success(self,data_json):
        result = json.loads(data_json)['result']
        error_code = result['error_code']
        error_extra_info = result['error_extra_info']
        if(error_code==0):
            print 'this request post data successed '
            return True
        else:
            print 'this request post data faild ,because ' + error_extra_info
            return False        


    def init_queue(self, host, userid, password, exchange_name):
        """
        Constructor. Initiate connection with the RabbitMQ server.

        @param exchange_name name of the exchange to send messages to
        @param host RabbitMQ server host 
        @param userid RabbitMQ server username
        @param password RabbitMQ server user's password
        """
        self.exchange_name = exchange_name
        self.connection = amqp.Connection(host=host, userid=userid,
            password=password, virtual_host="/", insist=False)
        if (self.connection ) :
            self.channel = self.connection.channel()
        else :
            #print (' connection rabbitMQ faild ')
            flag = faild
    #put message        
    def publish_message(self, routing_key, message, json_type):
        """
        Publish message to exchange using routing key
        
        @param text message to publish
        @param routing_key message routing key
        """
        try :
            msg = amqp.Message(message)
            msg.properties["content_type"] = "text/plain"
            msg.properties["delivery_mode"] = 2
            msg.properties["priority"] = 0
            msg.properties["application_headers"] = {'GSON_TYPE': json_type}
            msg.properties["content_encoding"] = "UTF-8"
            #exchange is not null then undo put msg to queue
            self.channel.basic_publish(exchange='',
                               routing_key=routing_key, msg=msg)
        except Exception,e :
            print e
    
    #get queue size
    def get_msgcount(self,queue):
        try:
            declareOk = self.channel.queue_declare(queue)
            return declareOk.getMessageCount()
        except Exception,e:
            print e
    
    #close connection        
    def close_conn(self):
        """
        Close channel and connection
        """
        self.channel.close()
        self.connection.close()


if __name__ =='__main__':
   a = AssertCommon()
   #flag = 'true'
   a.Assert_False(False)
   result=()
   a.Assert_Null(result)
