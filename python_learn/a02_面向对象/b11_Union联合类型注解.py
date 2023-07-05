"""    
    @author: fosss
    Date: 2023/7/5
    Time: 16:21
    Description: 数据类型为Union中的之一
"""
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "32"]


def fun(data: Union[int, str]) -> Union[int, str]:
    pass
