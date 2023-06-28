# 自定义求字符串长度的函数
str = "2jowjrjawjf"


def my_len(str):
    """
    对函数功能进行说明
    :param str: 对这个参数进行说明
    :return: 对返回值进行说明
    """
    count = 0
    for i in str:
        count += 1
    print("长度为：", count)


my_len(str)

# 局部变量，全局变量
num = 3000


def test_a():
    num = 10
    print(f"test_a:{num}")


test_a()
print(num)


def test_b():
    global num  # 将num设置为全局变量
    num = 10
    print(f"test_b:{num}")


test_b()

print(num)

# 综合案例-黑马ATM
account = 5000000


def getAccount():
    """
    查询余额
    :return:
    """
    print("-------------查询余额---------------")
    print(f"周杰轮，您好，您的余额剩余：{account}元")


def deposit(money):
    """
    存款
    :param money:
    :return:
    """
    global account
    account += money
    print(f"周杰轮，您好，您存款{money}元成功，余额剩余：{account}元")


def withdrawal(money):
    global account
    account -= money
    print(f"周杰伦，您好，您取款{money}元，余额剩余：{account}元")


print("-----------------主菜单--------------")
print("周杰轮，您好，欢迎来到黑马银行ATM.请选择操作：")
print("查询余额  [输入1]")
print("存款     [输入2]")
print("取款     [输入3]")
print("退出     [输入4]")
in_put = int(input("请输入您的选择："))

if in_put == 1:
    getAccount()
elif in_put == 2:
    deposit(50000)
elif in_put == 3:
    withdrawal(50000)
else:
    print("退出")
