#!/usr/bin/python3.4
# coding=utf-8

#print('Python', python_version())
print('3 / 2 =', 3 / 2)


#从任意长度的可迭代对像中分解元素, 使用*
#1.eg:去除成绩中的第一个与第二个成绩

def avg(x):
    return sum(x)/len(x)
def drop_first_last(grades):
    first,*middle,last = grades
    return avg(middle)




if __name__ == '__main__':
    grades = [12,34,45,45,54]
    t = drop_first_last(grades)
    print(t)
