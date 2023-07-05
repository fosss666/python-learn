"""    
    @author: fosss
    Date: 2023/7/5
    Time: 18:29
    Description: 实体类
"""


class Record:
    """创建记录实体"""

    def __init__(self, date: str, order_id: str, money: int, province: str):
        self.date = date  # 时间
        self.order_id = order_id  # 订单号
        self.money = money  # 销售额
        self.province = province  # 省

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"


if __name__ == '__main__':
    r = Record("1", "1", 1, "1")
    print(r)
