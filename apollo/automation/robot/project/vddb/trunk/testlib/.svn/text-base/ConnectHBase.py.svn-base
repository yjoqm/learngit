#!/usr/bin/python
#coding: utf-8
import sys  
import time  
from thrift import Thrift  
from thrift.transport import TSocket, TTransport  
from thrift.protocol import TBinaryProtocol  
from hbase import ttypes  
from hbase.Hbase import * 

class ConnectHBase:
    ''' sample:
    def main(self):
        LE=sys.argv
        print LE[0]
        client = connect_hbase()
        print '\n'
        print "*******************************************"
        #create_all_tables(client)  
        list_all_tables(client)
        print '-----------------------table[sid_tids]-------------------'
        task_id=getOneRow(client,"sid_tids",LE[1],"t:task_uuids")
        print 'task_id:',task_id
        if task_id!=None:
            task_id=task_id[2:len(task_id)-2]
            print '------------------------table[task]----------------------'
            task_result=getOneRow(client,"task",task_id,"i:site_asset_id")
            print task_result
            print '-----------------------table[finished]--------------------'
            finish_match=getOneRow(client,"finished",task_id,"f:is_match")
            finish_status=getOneRow(client,"finished",task_id,"f:query_status")
            print"finished data:(is_match,query_status)(%s,%s)"%(finish_match,finish_status)
        print "*******************************************"
        print '\n'

    def test_url(self):
        LE=sys.argv
        print LE[1]
        print '\n'
        print "*******************************************"
        client = connect_hbase()
        task_id=getTaskId(client,"task",LE[1])
        print task_id
        if task_id!=None:
            #task_id=task_id[2:len(task_id)-2]
            print '------------------------table[task]----------------------'
            task_result=getOneRow(client,"task",task_id,"i:site_asset_id")
            #print task_result
            print '-----------------------table[finished]--------------------'
            finish_match=getOneRow(client,"finished",task_id,"f:is_match")
            finish_status=getOneRow(client,"finished",task_id,"f:query_status")
            print"finished data:(is_match,query_status)(%s,%s)"%(finish_match,finish_status)
        print "*******************************************"
        print '\n'

    def main_scan(self):
        client = connect_hbase()
        scann_table(client,"sid_tids","task_uuids")
    '''
    def create_all_tables(self,host,port): 
        client=self.connect_hbase(host,port)
        '''store table'''  
        table_name = 'store_table'  
        col_name = ['store:']  
        create_table(client, table_name, col_name)  
        table_name2 = 'item_table'  
        col_name2 = ['item:', 'item_page:']  
        create_table(client, table_name2, col_name2)  
    def drop_all_tables(self,host,port): 
        client=self.connect_hbase(host,port)
        tables = ['store_table', 'item_table']  
        for table in tables:  
            if client.isTableEnabled(table):  
                print "    disabling table: %s"  %(table)  
                client.disableTable(table)  
            print "    deleting table: %s"  %(table)  
            client.deleteTable(table)  
    def create_table(self,host,port,table_name, table_desc): 
        client=self.connect_hbase(host,port) 
        columns = []  
        for name in table_desc:  
            col = ColumnDescriptor(name)  
            columns.append(col)  
        try:  
            print "creating table: %s" %(table_name)  
            client.createTable(table_name, columns)  
        except AlreadyExists, ae:  
            print "WARN: " + ae.message  
        except Exception, e:  
            print "error happend: " + str(e)  
    def list_all_tables(self,host,port):
        client=self.connect_hbase(host,port)  
        # Scan all tables  
        print "scanning tables..." 
        print "table names:%s"%(client.getTableNames()) 
        #for t in client.getTableNames():  
        #    print "  -- %s" %(t)  
        #    cols = client.getColumnDescriptors(t)  
        #     print "  -- -- column families in %s" %(t)  
        #     for col_name in cols.keys():  
        #        col = cols[col_name]  
        #        print "  -- -- -- column: %s, maxVer: %d" % (col.name, col.maxVersions) 
    def getOneRow(self,host,port,table,rowKey,colsKey):
        client=self.connect_hbase(host,port)
        result = client.getRow(table, rowKey)
        x_value=None
        #print result
        for r in result:
            print 'the   row  is: ' , r.row
            x_value=r.columns.get(colsKey).value
            print 'the  value is: ' , x_value
        return x_value
    def connect_hbase(self,host,port):  
        # Make socket  
        # transport = TSocket.TSocket('182.92.153.94', 9090) 
        transport = TSocket.TSocket(host, port)  
        # Buffering is critical. Raw sockets are very slow  
        transport = TTransport.TBufferedTransport(transport)  
        # Wrap in a protocol  
        protocol = TBinaryProtocol.TBinaryProtocol(transport)  
        # Create a client to use the protocol encoder  
        client = Client(protocol)  
        # Connect!  
        transport.open()  
        return client  
    def printRow(self,entry):  
        print "row: " + entry.row + ", cols:",  
        for k in sorted(entry.columns):  
            print k + " => " + entry.columns[k].value,  
        print "/n"  

    def isMatch(self,entry,url):
        match_result=False
        for k in sorted(entry.columns):  
            #print k + " => " + entry.columns[k].value
            if entry.columns[k].value.find(url)>0:
               match_result=True
               break
        return match_result

    def scann_table(self,host,port,table,colsKey):  
        client=self.connect_hbase(host,port)
        #t = 'sid_tids'
        print 'scan [%s] ...'%(table)
        columnNames = []  
        for (col, desc) in client.getColumnDescriptors(table).items():  
            print "column with name: "+desc.name  
            print desc  
            columnNames.append(desc.name+colsKey)  
        print columnNames  
          
        print "Starting scanner..."  
        scanner = client.scannerOpenWithStop(table, "", "", columnNames)  
          
        r = client.scannerGet(scanner)  
        i = 1  
        while r: 
            if r != []:
                print r[0] 
            if i % 100 == 0:  
                printRow(r[0])  
            r = client.scannerGet(scanner) 
            i += 1  
          
        client.scannerClose(scanner)  
        print "Scanner finished, total %d row" % (i-1)  
    def getTaskId(self,host,port,table,url):
        client=self.connect_hbase(host,port)
        #t = 'sid_tids'
        print 'scan [%s] ...'%(table)
        columnNames = []  
        for (col, desc) in client.getColumnDescriptors(table).items():  
            #print "column with name: "+desc.name  
            #print desc  
            columnNames.append(desc.name+"extra_info")  
        #print columnNames  
          
        print "Starting scanner..."  
        scanner = client.scannerOpenWithStop(table, "", "", columnNames)  
          
        r = client.scannerGet(scanner) 
        task_id=None 
        i = 1  
        while r: 
            if r == []:
               break 
            if self.isMatch(r[0],url):
               print r
               task_id=r[0].row
               break
     
            r = client.scannerGet(scanner) 
            i += 1  
          
        client.scannerClose(scanner)  
        return task_id
