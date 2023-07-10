"""    
    @author: fosss
    Date: 2023/7/10
    Time: 18:53
    Description:
"""
import re

string = "itheima itcast python python"
# match方法
print(re.match("python", string))

match = re.match("ithe", string)
print(match)
print(match.span())

# search方法
search = re.search("python", string)
print(search)
print(search.span())

# findAll方法
findAll = re.findall("python", string)
print(findAll)
