#!/usr/bin/env python
# coding=utf-8
def sage_float(obj):
    try:
        retral = float(obj)
    except ValueError:
        retral = 'could not convert non-number to float'
    except TypeError:
        retral = 'tayape could not convert non-number to float'
    return retral

