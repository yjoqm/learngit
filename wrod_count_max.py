#!/usr/bin/env python
# coding=utf-8

import re

#从文件中读取数据，返回字符串
def file_read(filename):
    with open(filename,'r') as f:
        article = f.read()
    return article

#返回英文单词列表
def word_list(string):
    words = re.findall(r'[a-zA-Z]+\b',string)
    return words

#计算出现次数最多的单词

def most_word_number(word_list):
    str_dict = {}
    for item in word_list:
        if item in str_dict:
            str_dict[item] += 1
        else:
            str_dict[item] = 1
            str_dict = {str_dict[key]:key for key in str_dict}   #去重 返回 {1: 'software', 2: 'million', 3: 'of', 4: 'the', 5: 'GitHub', 7: 'and'}
    return (max(str_dict),str_dict[max(str_dict)])



if __name__ == '__main__':
    string = file_read('/Users/admin/mygit/learngit/github.txt')
    words = word_list(string)
    times,words =  most_word_number(words)
    print times, words
    


