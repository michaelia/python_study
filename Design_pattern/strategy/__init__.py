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

if __name__ == '__main__' :

# 测试第一种CashNormal策略
    strategy = CashNormal()
    contextone=context(strategy)
    print(contextone.contextInterface(500))

# 测试第二中
    stratetwo= CashRebate(300,100)
    contexttwo = context(stratetwo)
    print(contexttwo.contextInterface(400))

# 测试第三种
    stratethree = CashRetun(0.8)
    contextthree = context(stratethree)
    print(contextthree.contextInterface(400))