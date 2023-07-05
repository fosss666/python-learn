"""    
    @author: fosss
    Date: 2023/7/5
    Time: 12:08
    Description:
"""
import random

# 1. :+数据类型方式
# num: int = 10
# my_list: list = [1, 2, 3]
# my_list2: list[int] = [1, 2, 3]
# my_tuple: tuple[str, str, str] = ("1", "2", "3")
# my_dict: dict[int, str] = {1: '1'}
# x: int = random.randint(1, 10)

# 2. 注解方式
num = 10  # type: int
my_list = [1, 2, 3]  # type: list
my_list2 = [1, 2, 3]  # type:list[int]
my_tuple = ("1", "2", "3")  # type:tuple[str,str,str]
my_dict = {1: '1'}  # type: dict[int:str]
x = random.randint(1, 10)  # type:int
