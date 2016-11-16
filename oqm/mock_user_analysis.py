#!/usr/bin/env python
# coding=utf-8
import random,string,os,re,hashlib

def randomString(choice, length):
    list = []
    for i in range(length):
        if choice == 'ld':
            list.append(random.choice(string.ascii_lowercase + string.digits))
        elif choice == 'ud':
            list.append(random.choice(string.ascii_uppercase + string.digits))
        elif choice == 'd':
            list.append(random.choice(string.digits))
        elif choice == 'l':
            list.append(random.choice(string.ascii_lowercase))
        elif choice == 'u':
            list.append(random.choice(string.ascii_uppercase))
        elif choice == 'uld':
            list.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits))
    st = ''.join(list)
    return st

def randomZid():
    reobj = re.compile(r'^[0-9a-f]{32}$')
    while(1):
        list = []
        for i in range(32):
            list.append(random.choice('abcdef' + string.digits))
        cookie = ''.join(list)
        match = reobj.search(cookie)
        if match:
            return match.group()

def randomStamp():
    return str(random.randint(1478620799,1478844323)) #08 23:59:59~11.11 14:5:23


if __name__ == '__main__':
    seg = {}
    temp = randomZid()
    with open('/Users/admin/Documents/data/mock_profile/mock_profile5.txt', 'w') as file:
        for i in range(10000):
            if random.randint(1,3) == 1:
                zid = randomZid()
            else:
                zid = temp
            temp = zid
            stamp = randomStamp()
            new = str(random.randint(0,1))
            file.write('\t'.join([zid,stamp,new]))
            file.write(os.linesep)
        file.close()
