#encoding:utf-8
import os
findpath="/usr/local/"
def findconf(findpath):
    p_list=[]
    for i in os.walk(findpath):
        for j in i[2]:
            if ".conf" in j:
#                print i[0]+"/"+i[2][0]
                #print j
                filename=i[0]+"/"+j
                with open(filename) as f:
                    for line in f:
                        if ':' in line:
                            p=line.strip().split(":")
                            if p[-1].isdigit():
                                if p[-1] not in p_list:
                                    p_list.append(p[-1])
    print " finenema: %s and port is %s: " %(f, p_list)

findconf(findpath)
