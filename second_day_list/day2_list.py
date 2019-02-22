#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys as sys
# list1= ['physics', 'chemistry', 1997, 2000]
# list1[2]='englist'
# print(list1)


# list1 = ['a',1,2,'one']
# del list1


# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort(reverse = True)
# print(vowels)
#
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# random.sort(key=lambda x:x[1])
# print(random)

# P1= P=[1,2,3,4,5,6,7]
# print(P1)
# P1.append(8)
# print("修改后的p1:",P1,"&修改前的p:",P)
#
# P2=P1[:]
# P2.append(9)
# print(P2,P)

# def fab(max):
#    n, a, b = 0, 0, 1
#    while n < max:
#        print(b)
#        a, b = b, a + b
#        n = n + 1
# fab(5)

# 为了不让print 降低效率，所以生成列表
def fab1(max):
   n, a, b = 0, 0, 1
   L = []
   while n < max:
       L.append(b)
       a, b = b, a + b
       n = n + 1
   return L
fablist=fab1(15)
k=list(map(lambda x: print(x),fablist))
print(sys.getsizeof(k))

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

g=list(map(lambda x: print(x),fab(15)))
g
print(sys.getsizeof(g))