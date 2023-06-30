# 限制import *的导入范围
__all__ = ['test1']


def test1():
    print("test1")


def test2():
    print("test2")


# 防止导入该模块后自动执行下面的语句
if __name__ == '__main__':
    test1()
