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
class OperationFactory(ABC):

    @abstractmethod
    def createOpeation(self):
        pass


class AddFactory(OperationFactory):

    def createOpeation(self):
        return OperationAdd()


class SubFactory(OperationFactory):
    def createOpeation(self):
        return OperationSub()

class MulFactory(OperationFactory):

    def createOpeation(self):
        return OperationMul()

class DivFactory(OperationFactory):

    def createOpeation(self):
        return OperationDiv()

if __name__ == '__main__' :
    # 抽象工厂类，则
    addFactory = AddFactory().createOpeation()
    addFactory._numberA=10
    addFactory._numberB=15
    # print("111")
    print(addFactory.GetResult())

