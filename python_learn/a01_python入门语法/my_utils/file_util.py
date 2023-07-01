"""
文件相关操作
"""


def print_file_info(file_name):
    """
    接受传入文件的路径，打印内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    :param file_name:
    :return:
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f.read())
    except Exception as e:
        print(f"文件不存在:{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)


if __name__ == '__main__':
    print_file_info("E:/fo的python学习/python_learn/a01_python入门语法/word1.txt")
    # append_to_file("E:/fo的python学习/python_learn/a01_python入门语法/word.txt", "\n哈哈哈哈")
