# 函数参数的传递
# 1.位置参数
def f1(name, age, id):
    print(f"name:{name},age:{age},id:{id}")


f1('张三', 18, 222)
# 2.关键字传递
f1(name='里斯', age=9, id=22)


# 3.默认值
def f1(name, age, id=0):
    print(f"name:{name},age:{age},id:{id}")


f1('wangwu', 18)


# 4.不定长-位置传递
def f1(*args):
    print(f"参数类型是：{type(args)},内容为：{args}")


f1(12, 3, 4)


# 5.不定长-关键字传递
def f1(**args):
    print(f"参数类型是：{type(args)},内容为：{args}")


f1(name="张三", age=11)


# 函数作为参数传递
def f1(f2):
    res = f2(1, 2)
    print(res)
    print(type(f2))


def f2(n1, n2):
    return n1 + n2


f1(f2)
