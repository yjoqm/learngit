#!/usr/bin/env python
# coding=utf-8
def out_max(*values):
    if not values:
        return None
    m = values[0]
    for v in values[1:]:
        if v > m:
            m = v
    return m

if __name__=='__main__':
    test = out_max(2,1,3,5,67,3,-1)
    print test
