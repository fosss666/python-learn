# 列表 元素类型不受限
# liebiao = ['itheima', 666, True]
# print(liebiao)
# print(type(liebiao))
# arr2 = [[1, 2, 3], [2, 3, 4]]
# print(arr2)
# print(liebiao[1])
# print(arr2[0][0])
# 列表的反向索引 -1 -2 -3
# print(liebiao[-2])
# 列表常用操作
# l = [21, 25, 21, 23, 22, 20]
# l.append(31)  # 追加数字到列表尾部
# l.extend([29, 33, 30])  # 追加新列表到尾部
# print(l[0])  # 第一个元素
# print(l[-1])  # 最后一个元素
# print(l.index(31))  # 查找元素31的下标
# del l[0]  # 删除第一个元素
# l.pop(-1)  # 删除最后一个元素
# l.remove(25)  # 删除第一个出现的该元素
# print(l.count(1))  # 查看某元素个数
# print(len(l))  # 查看元素总个数
# l.clear()  # 清空列表
# print(l)

# 元组 不可被修改
# my_tuple = ('周杰伦', 11, ['football', 'music'])
# print(my_tuple.index(11))
# print(my_tuple[0])
# my_tuple[2].pop(0)
# my_tuple[2].append('coding')
# print(my_tuple)

# 字符串 不可被修改，替代操作会返回一个新字符串
# my_str = "12fjalsjfaj21"
# new_my_str = my_str.strip("12")
# print(new_my_str)
# 案例-分割字符串
# my_str = "itheima itcast boxuegu"
# print(my_str.count("it"))
# my_str = my_str.replace(" ", "|")
# print(my_str)
# print(my_str.split("|"))

# 序列切片
my_str = "万过薪月，员序程马黑来，nohtyP学"
print(my_str[9:4:-1])
my_str = my_str.split("，")[1]
print(my_str.replace("来", "")[::-1])
