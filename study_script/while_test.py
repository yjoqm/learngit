#!/usr/bin/env python
# coding=utf-8

def get_input(raw_input_text,input_type):
    right_input = False
    while not right_input:
        try:
            input_data = raw_input("%s:" % raw_input_text)
            input_data = eval("%s('%s')" % (input_type,input_data))
        except:
            print("type error[%s]" % input_type)
        else:
            right_input = True
    return input_data

def main():
    feed_id = get_input("feed_id", "int")


if __name__ == '__main__':
    main()
