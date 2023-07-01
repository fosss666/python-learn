"""
字符串相关操作
"""


def str_reverse(s):
    """
    字符串翻转
    :param s:
    :return:
    """
    return s[::-1]


def substr(s, x, y):
    """
    字符串切片
    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]


if __name__ == '__main__':
    s = str_reverse("asdf")
    print(s)
    s = substr("asdf", 0, 2)
    print(s)
