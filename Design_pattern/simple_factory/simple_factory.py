#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
import pdb
# ➕ 、减、乘、除类分离

# 为了操作类独立化，新增一种操作、不透露其他操作的实现原理，可以进行隔离

@dataclass
class Operation(ABC):

    _numberA:Number  =2
    _numberB: Number =2

    @abstractmethod
    def GetResult(self):
        result=0
        pdb.set_trace()
        return result

class OperationAdd(Operation):

    def GetResult(self):
        rusult=self._numberA+self._numberB
        print("11")
        return rusult


class OperationSub(Operation):

    def GetResult(self):
        rusult=self._numberA-self._numberB
        return rusult


class OperationMul(Operation):

    def GetResult(self):
        rusult=self._numberA*self._numberB
        return rusult

class OperationDiv(Operation):

    def GetResult(self):
        if  self._numberB:
            raise "除数不能为0"
        rusult=self._numberA/self._numberB
        return rusult

@dataclass
class OperationFactory():

    def createOpeation(self,operation):

        operationList = {
            "add": OperationAdd(),
            "sub": OperationSub(),
            "mul": OperationMul(),
            "div": OperationDiv()
        }

        if not operationList.get(operation):
            raise "清输入正确的"
        return operationList[operation]

if __name__ == 'main':
    # 简单的工厂模式，即是把工厂类简单的分类判断，如果需要新增一个方法，则需要改动原来的代码，这会作为涉及违法了开放原则，所以我门改为把工厂抽象画
    factory =OperationFactory().createOpeation("add")
    factory._numberA=5
    factory._numberB=5
    print(factory.GetResult())

