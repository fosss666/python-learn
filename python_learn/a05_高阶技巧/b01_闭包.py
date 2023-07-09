"""    
    @author: fosss
    Date: 2023/7/9
    Time: 13:50
    Description:优点，使用闭包可以让我们得到：
                无需定义全局变量即可实现通过函数，持续的访问、修改某个值
                闭包使用的变量的所用于在函数内，难以被错误的调用修改

                缺点：
                由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一直占用内存

"""


def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


f = outer("logo")
f("这呵呵呵")
f("lll")


# 修改外部函数的参数
def outer(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner


f = outer(1)
f(2)
f(3)


# 取款案例
def account_do(account=0):
    def do(money, deposit=True):
        nonlocal account
        if deposit:
            account += money
            print(f"存款：{money},余额：{account}")
        else:
            account -= money
            print(f"取款：{money},余额：{account}")

    return do


f = account_do()
f(10)
f(5, deposit=False)
