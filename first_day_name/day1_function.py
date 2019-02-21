#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

# def printme( str ):
#     print(time.time(),':',str,"a")
#     return

# print(printme( u"周末快乐" ))

#必备参数
def say(sayContont,sayWho):
    print(sayWho,":",sayContont)
# print(say("你好","小名"))

#可变参数
def change_canshu(list1):
    list1.append('newStr')
    print('调用前的参数:','{}'.format(list1))
# change_canshu([1,2,3])

def say(message, times = 1):
    print(message * times )
# say('gloryroad!',3)


def printMax(x, y):
    '''打印两个数中的最大值。

    两个值必须都是在整形数。'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, '最大')
    else:
        print(y, '最大')

# print(printMax(3,5))
#
# print(printMax.__doc__)

