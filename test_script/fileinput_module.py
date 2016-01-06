#!/usr/bin/env python
# coding=utf-8
import fileinput
import os

def get_file_content(files):
    '''读取（多个）文件的内容，以字条串的形式返回'''

    if files != None:
        lines = ''
        with fileinput.input(files) as fp:
            for line in fp:
                lines += line
    else:
        print 'file is None'

def get_file_name(file):
    '''只有当文件被读的时候才会取得filename,否则返回None'''
    if os.path.exists(file) and os.path.isfile(file):
        names = []
        for line in fileinput.input(file):
            name = fileinput.filename()
            if name != None:
                fileinput.nextfile()
            names.append(name)
            return names
    else:
        print 'path [{}] is not exists~'.format(file)




def main():
    files = 'outerid.txt,test.py'
    file = 'test.py'
    content = get_file_content(files)
    print content
    name = get_file_name(file)
    print name

if __name__ == '__main__':
    main()



    



