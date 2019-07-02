#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Strategy(ABC):
    @abstractmethod
    def acceptCash(self,money):
        return money

class CashNormal(Strategy):

    def acceptCash(self,money):
        return money

class CashRebate(Strategy):

    def __init__(self,moneyCondition,moneyReturn):
        self.moneyCondition=moneyCondition
        self.moneyReturn=moneyReturn

    def acceptCash(self,money):
        if money > self. moneyCondition:
            money -= self.moneyReturn
        return money

@dataclass
class CashRetun(Strategy):

    moneyCondition:float

    def acceptCash(self,money):
        return money*self.moneyCondition

@dataclass
class context():

    strategy:Strategy

    def contextInterface(self,monkey):
        return  self.strategy.acceptCash(monkey)



@dataclass
class contextFactory():

    def createOpeation(self,operation,monkey=0,reback=0,rerate=0,reCondition=0):
        operationList={
            "normal":CashNormal(),
            "rebate":CashRebate(reback,rerate),
            "csreturn":CashRetun(reCondition)
        }

        if operation != "" or None:
            return context(operationList[operation]).contextInterface(monkey)

        return " "


if __name__ == '__main__' :

    cf=contextFactory()

# 测试第一种CashNormal策略
    print(cf.createOpeation("normal",500))

# 测试第二中
    print(cf.createOpeation("rebate",500,300,100))
#
# # 测试第三种
#     stratethree = CashRetun(0.8)
#     contextthree = context(stratethree)
#     print(contextthree.contextInterface(400))