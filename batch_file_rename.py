#!/usr/bin/env python
# coding=utf-8
#  Description : This will batch rename a group of files in a given directory, once you pass the current and new extensions
import os
import sys
work_dir = sys.argv[1]
old_ext = sys.argv[2]
new_ext = sys.argv[3]

files = os.listdir(work_dir)
for filename in files:
    file_ext = os.path.splitext(filename)[1]
    if old_ext == file_ext:
        newfile = filename.replace(old_ext,new_ext)
        os.rename(os.path.join(work_dir,filename),os.path.join(work_dir,newfile)



