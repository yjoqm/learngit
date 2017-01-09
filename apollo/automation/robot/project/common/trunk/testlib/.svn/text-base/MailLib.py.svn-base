# -*- coding: utf-8 -*-
import imaplib
import email
import os
from binascii import *




class MailLib:
    def __init__(self):
        pass
    
    
    def set_mail_server(self, username, password, host, port = "default", ssl = "ssl"):
        if ssl.lower() != "none":
            if port == "default":
                port = imaplib.IMAP4_SSL_PORT
            else:
                port = int(port)
            self.server = imaplib.IMAP4_SSL(host, port)
        else:
            if port == "default":
                port = imaplib.IMAP4_PORT
            else:
                port = int(port)
            self.server = imaplib.IMAP4(host, port)
        
        self.server.login(username, password)
        
    def select_mail(self, from_addr, order = "desc", limit = "all"):
        self.mail_number = 0
        self.attachment = []
        self.server.select("INBOX", True)
        typ, data = self.server.search(None, '(FROM "%s")' % from_addr)
        if order == "desc":
            order = -1
        elif order == "asc":
            order = 1
        else:
            raise AssertionError("order should be 'desc or asc'")
        
        if limit == "all":
            limit = len(data[0].split())
        else:
            limit = int(limit)
        data = data[0].split()[::order][:limit]
        mail_list = []
        for item in data:
            typ, mail_data = self.server.fetch(item, '(RFC822)')
            message = email.message_from_string(mail_data[0][1])
            mail = self.__mail_parse(message)
            mail_list.append(mail)
            self.mail_number += 1
            
        self.server.close()
        return mail_list
    
    def logout_server(self):
        self.server.logout()
    
    def __mail_parse(self, email_format_data):
        mail_info = {}
        self.__header_parse(email_format_data, mail_info)
        self.__body_parse(email_format_data, mail_info)
        return mail_info
        #print mail_info
        
        
    def __header_parse(self, message, mail_info):
        mail_info["subject"] = self.__char_decode(message.get("subject"))
        mail_info["from"] = self.__mail_addrparse("from", message)
        mail_info["to"] = self.__mail_addrparse("to", message)
        mail_info["cc"] = self.__mail_addrparse("cc", message)
        
    def __mail_addrparse(self, name, message):
        ret_value = ""
        addr_list = message.get(name, "").split(",")
        for item in addr_list:
            mail_addr = email.utils.parseaddr(item.strip())[1]
            if ret_value != "":
                ret_value += ", "
            ret_value += mail_addr
        return ret_value
        
    def __body_parse(self, message, mail_info):
        for part in message.walk():
            if not part.is_multipart():
                content_type = part.get_content_type()
                file_name = part.get_filename()
                charset = None
                for item in part.get("Content-Type").replace(" ", "").replace("\r\n", "").replace("\t", "").replace("\n", "").split(";"):
                    if item.startswith("charset="):
                        charset = item[8:]
                
                if file_name:
                    #print "attach file: " + self.__char_decode(file_name)
                    attach = []
                    attach.append(self.mail_number)
                    attach.append(self.__char_decode(file_name))
                    attach.append(part.get_payload(decode=True))
                    self.attachment.append(attach)
                    pass
                else:
                    if charset:
                        mail_info["content"] = part.get_payload(decode=True).decode(charset)
                    else:
                        mail_info["content"] = part.get_payload(decode=True)
                    pass
        pass
    
    
    def __char_decode(self, message):
        dh = email.Header.decode_header(email.Header.Header(message))
        charstring = ""
        for item in dh:
            if not item[1]:
                charstring += item[0]
            else:
                charstring += item[0].decode(item[1])
        return charstring
    
    def save_attachments(self, path, index, override = "true"):
        index_list = range(self.mail_number)
        if index == "all":
            index = "[:]"
        try:
            if len(index[1:-1].split(":")) == 1:
                index_list = eval(index)
            else:
                index_list = eval("index_list%s" % index)
        except Exception,ex:
            raise AssertionError("argument 'index' format error")
        if os.path.exists(path):
            for attach in self.attachment:
                if attach[0] in index_list:
                    file_name = path + "/" + attach[1]
                    if not os.path.exists(file_name) or override.lower() == "true":
                        fp = open(path + "/" + attach[1], "wb")
                        fp.write(attach[2])
                        fp.close()
        else:
            raise AssertionError("No such directory %s" % path)
        
        
        
        
        
    
if __name__ == '__main__':
    mail = MailLib()
    mail.set_mail_server("yan_jiawei@vobile.cn","vobile","mail.vobile.cn")
    mail_list = mail.select_mail("yan_jiawei@vobile.cn", "desc", "1")
    for i in mail_list:
        print "*" * 100
        print i.get("content")
    print mail_list
    mail.logout_server()
    