#!/usr/bin/env python
# coding=utf-8
import os
import re  
import fileinput  
import fnmatch  

#Python实现多个文件中替换字符串
#fileinput中的inplace=True表示把输出重定向到文件。这样所有print输出都是指向文件的


def walkDir(directory, ext='*.*', topdown=True):  
    fileArray = []  
    for root, dirs, files in os.walk(directory, topdown):  
        for name in files:  
            if fnmatch.fnmatch(name, ext):  
                fileArray.append(os.path.abspath(os.path.join(root, name)))  
    return fileArray  
  
def replaceInFile(filename, strFrom, strTo):  
    for line in fileinput.input(filename, inplace=True):  
        if re.search(strFrom, line):  
            line = line.replace(strFrom, strTo)  
        print line,  
  
if __name__ == '__main__':  
    for filename in walkDir('.', '*.txt'):  
        replaceInFile(filename, 'abc', 'cba') 
