"""    
    @author: fosss
    Date: 2023/7/4
    Time: 21:21
    Description:
"""


class Phone:
    time = None
    model = None

    def call_by_4g(self):
        print("用4g打电话")


class NFC:
    time = None
    model = None

    def open(self):
        print("开启nfc")

    def close(self):
        print("关闭nfc")


class Phone2023(Phone, NFC):
    pass  # 表示没有新增变量和方法


phone = Phone2023()
phone.open()
