#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from  dataclasses import  dataclass
from dataclasses import field
import abc

# @dataclass
# class Number:
#     val:int
# one =Number(1)
# print(one.val)


def test_ic(favourite_ic: str) -> str:
    user_guess: str = input("Try to guess our favourite IC >>> ")
    breakpoint()

    if user_guess == favourite_ic:
        return "Yup, that's our favourite!"
    else:
        return "Sorry, that's not our favourite IC"


# if __name__ == '__main__':
#     favourite_ic: int = 555
#     print(test_ic(favourite_ic))


# class User:
#     def __init__(self, name: str, age: int, favourite_ic: str) -> None:
#         self.name = name
#         self.age = age
#         self.favourite_ic = favourite_ic
#
#     def is_adult(self) -> bool:
#         """Return True if user is an adult, else False."""
#         return self.age >= 18



#     3.7支持的写法
@dataclass
class User:
    name:str
    favourite_ic: str
    age:int = field(default = 0)
    mark :List[int]=field(default=0)


@dataclass
class Preson(metaclass=abc.ABCMeta):
    name:str


class MyException(Exception):
    def __init__(self, *args):
        self.args = args


# raise MyException('爆出异常吧哈哈')

# 常见做法定义异常基类,然后在派生不同类型的异常

class loginError(MyException):
    def __init__(self, code=100, message='登录异常', args=('登录异常',)):
        self.args = args
        self.message = message
        self.code = code


class loginoutError(MyException):
    def __init__(self):
        self.args = ('退出异常',)
        self.message = '退出异常'
        self.code = 200


# raise loginError() # 这里突然返现 raise引发的异常将中断程序
#

if __name__ == '__main__':
    # john = User('John',  '555')
    # # print(john.__dict__)
    # print('He is name : {},age:{},favourite_ic:{}'.format(john.name, john.age, john.favourite_ic))
    try:
        raise loginError()
    except loginError as e:
        print(e)  # 输出异常
        print(e.code)  # 输出错误代码
        print(e.message)  # 输出错误信息