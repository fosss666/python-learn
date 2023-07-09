"""    
    @author: fosss
    Date: 2023/7/9
    Time: 14:55
    Description:
"""
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    import threading

    t1 = threading.Thread(target=sing, args=("我在唱歌",))  # 加逗号是为了告诉python这是一个元组
    t2 = threading.Thread(target=dance, kwargs={"msg": "我在跳舞"})
    t1.start()
    t2.start()
