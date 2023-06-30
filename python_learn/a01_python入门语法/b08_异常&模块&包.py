# 异常
# try:
#     1 / 0
# except:
#     print("捕获到异常")
# try:
#     1 / 0
# except Exception as e:
#     print(f"捕获到异常:{e.args}")

# try:
#     print(name)
# except (ZeroDivisionError,NameError) as e:
#     print(f"捕获到异常:{e.args}")

# try:
#     print("执行：")
# except Exception as e:
#     print(f"捕获到异常:{e.args}")
# else:
#     print("没有异常")
# finally:
#     print("有没有异常都要执行")

# 异常的传递
def f1():
    print("f1执行")
    1 / 0
    print("f1结束")


def f2():
    print("f2执行")
    f1()
    print("f2结束")


def main():
    try:
        f2()
    except Exception as e:
        print(f"捕获到异常:{e}")


main()
