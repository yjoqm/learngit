#!/usr/bin/env python
# coding=utf-8
#计算最后一个周五

from datetime import datetime,timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday']

def get_previous_day(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    print 'day_num:',day_num
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num -day_num_target) % 7
    if days_ago == 0:
        days_ago =7
    target_date = start_date - timedelta(days=days_ago)
    return target_date



if __name__ == '__main__':
    t = get_previous_day('Monday',datetime(2016, 11, 15))
    print t
