"""    
    @author: fosss
    Date: 2023/7/4
    Time: 21:36
    Description:
"""


class Phone:
    time = "1"
    model = "六牌"

    def call_by_4g(self):
        print("用4g打电话")


class MyPhone(Phone):
    time = "11"
    model = "不留·牌"

    def call_by_4g(self):
        print(Phone.model)
        print(super().model)
        Phone.call_by_4g(self)
        super().call_by_4g()


phone = MyPhone()
phone.call_by_4g()
