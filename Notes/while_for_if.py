#!/usr/bin/env python
# coding=utf-8
number = 23
running = True

while running:
    guess = int(raw_input('Enter a integer: '))
    if guess == number:
        print('Congratuations, right')
        running = False
    elif guess < number:
        print "no ,it is a little higher than that"
    else:
        print "no,it is a liter lower than that"
else:
    print "the while loop is over."

#9*9表
str = ""
for i in range(1,10):
    for j in range(1,i + 1):
        str += ('%d * %d = %d\t'% (j,i,i*j))
    str += '\n'
print(str)



#continue

while True:
    s = raw_input('Enter something: ')
    if s == 'quit':
        break
    if len(s)< 3:
        print "input is not of suficient lenght"
        continue
print "lenght of the string is", len(s)



