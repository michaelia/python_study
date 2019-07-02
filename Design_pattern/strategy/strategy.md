`本章介绍策略模式`
##### 面向对象的编程，并不是类越多越好，类的划分是为了封装，但是分类的基础是抽象，具有相同属性和功能的对象的抽象的集合才是类

以下场景可以使用策略模式进行划分
 - 1、如果在一个系统里面有许多类，它们之间的区别仅在于它们的行为，那么使用策略模式可以动态地让一个对象在许多行为中选择一种行为。 
 - 2、一个系统需要动态地在几种算法中选择一种。 
 - 3、如果一个对象有很多的行为，如果不用恰当的模式，这些行为就只好使用多重的条件选择语句来实现。
 
 策略模式：定义了算法的家族，将其封装起来，让他们之间可以相互替换
 优点：
  - 1、算法可以自由切换。 
  - 2、避免使用多重条件判断。 
  - 3、扩展性良好。
  
  缺点：
  
  - 1、策略类会增多。 
  - 2、所有策略类都需要对外暴露。
  
  
  本例举例商城的计算，算法组：1、正常收费 2、满100减50 3、打8折
  、、、
  
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
  、、、
  
  以上是需要客户端实现判断使用那种策略子类，策略类拥有了根据对象来动态的决定方法的能力。<br>
  但是单纯的策略类有一大坏处，由于调用策略类需要先传入某个子类的对象，这就使得客户端代码与多个子类存在耦合。
  <br>为了客户端与各种子类的解耦，则可以采用工厂模式与策略模式结合--》具体：strategy_factory.py
  
 ```
 改为工厂类
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
```