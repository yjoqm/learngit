#!/usr/bin/env python
# coding=utf-8

line_count = 0
word_count = 0
character_counts = 0

with open('/Users/admin/mygit/learngit/englist_txt.txt') as f:
    for line in f:
        words = line.split()
        line_count += 1
        word_count += len(words)
        character_counts  += len(line)

print line_count
print word_count

import re

def count_the_words(file):
    with open(file) as f:
        text = f.read()
        words_list = re.findall('[a-zA-Z0-9]+',text)
        count = len(words_list)
    return count
