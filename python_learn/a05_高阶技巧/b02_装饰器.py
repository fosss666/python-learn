"""    
    @author: fosss
    Date: 2023/7/9
    Time: 14:09
    Description:类似于AOP
"""

#闭包
def outer(func):
    print("我睡觉了")
    func()
    print("我醒了")
    return func


@outer
def sleep():
    import random
    import time
    time.sleep(random.randint(1, 5))


sleep()
