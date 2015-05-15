#!/usr/bin/env python
# coding=utf-8
print '\n choose 1 to calculate the five number;\n choose 2 to calculate the average of the five number;\n choose 3 to quit the program'  

def add():
    li = []
    i = 0
    while i< 6:
        input_num=int(raw_input("please input the number:"))
        li.append(input_num)
        i += 1
    return sum(li)
    
def avg():
    li = []
    i = 0
    while i< 6:
        input_num=int(raw_input("please input the number:"))
        li.append(input_num)
        i += 1
    return float(sum(li)/5)

flag = int(raw_input("choice a number:"))
if flag ==1:
    add_result = add()
    print add_result
elif flag ==2:
    avg_result = avg()
    print avg_result
elif flag ==3:
     break
else:
    print "you have enter the wrong number"
