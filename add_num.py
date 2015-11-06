#!/usr/bin/env python
# coding=utf-8
import logging

import Image, ImageDraw, ImageFont

#im = Image.open('/Users/admin/me.jpg')
#print im.format, im.size 

def add_num(img):
    im = Image.open('/Users/admin/me.jpg')
    print im.format, im.size 

    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/Users/admin/ampnews-issue3_30.jpg', size=40)
    logging.debug('myfont')
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpg')
    print "success"
    return 0

if __name__ == '__main':
    im = Image.open('/Users/admin/me.jpg')
    print "im",im.format,im.size
    print add_num(im)
