"""    
    @author: fosss
    Date: 2023/7/5
    Time: 18:28
    Description:文件处理
"""
import json

from data_define import Record


class FileReader:
    """抽象类"""

    def read(self) -> list[Record]:
        """
        读取文件
        """
        pass


class TextFileReader(FileReader):
    """
    读取文本文件
    """

    def __init__(self, path):
        self.path = path

    def read(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        r: list[Record] = []
        for line in f.readlines():
            # 去除换行符
            line = line.strip()
            # 封装数据
            a = line.split(",")
            record = Record(a[0], a[1], int(a[2]), a[3])
            # 添加到返回值中
            r.append(record)
        # 关闭文件
        f.close()
        # 返回数据
        return r


class JsonFileReader(FileReader):
    """
    读取JSON文件
    """

    def __init__(self, path):
        self.path = path

    def read(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        r: list[Record] = []
        for line in f.readlines():
            # 去除换行符
            line = line.strip()
            d = json.loads(line)
            # 封装数据
            record = Record(d['date'], d['order_id'], int(d['money']), d['province'])
            # 添加到返回值中
            r.append(record)
        # 关闭文件
        f.close()
        # 返回数据
        return r


"""
测试
"""
if __name__ == '__main__':
    # fr = TextFileReader("E:/fo的python学习/python_learn/a02_面向对象/b13_数据分析案例/2011年1月销售数据.txt")
    fr = JsonFileReader("E:/fo的python学习/python_learn/a02_面向对象/b13_数据分析案例/2011年2月销售数据JSON.txt")
    fr.read()
