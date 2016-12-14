#!/usr/bin/python3.4
# coding=utf-8
#计算当前月份的日期范围

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)



a_day = timedelta(days=1)
first_day, last_day = get_month_range()
#while first_day < last_day:
#    print(first_day)
#    first_day =+ a_day 



	

#使用 calendar.monthrange() 函数来找出该月的总天数
#为日期迭代创建一个同内置的 range() 函数一样的函数
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2016, 12, 1), datetime(2016,12,8),timedelta(hours=6)):
    print(d)
