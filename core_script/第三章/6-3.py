#!/usr/bin/env python
# coding=utf-8
#输入一些数字,然后排序
def ABC(nums_1):
    return sorted(nums_1)

def main():
    nums_1 = []
    while True:
        try:
            n = int(raw_input("input num :> ").strip())
            nums_1.append(n)
        except:
            break
    print '', ABC(nums_1)
if __name__ == '__main__':
    main()

