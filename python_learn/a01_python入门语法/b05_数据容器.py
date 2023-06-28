# 列表 元素类型不受限
liebiao = ['itheima', 666, True]
print(liebiao)
print(type(liebiao))
arr2 = [[1, 2, 3], [2, 3, 4]]
print(arr2)
print(liebiao[1])
print(arr2[0][0])
# 列表的反向索引 -1 -2 -3
print(liebiao[-2])
# 列表常用操作
l = [21, 25, 21, 23, 22, 20]
l.append(31)  # 追加数字到列表尾部
l.extend([29, 33, 30])  # 追加新列表到尾部
print(l[0])  # 第一个元素
print(l[-1])  # 最后一个元素
print(l.index(31))  # 查找元素31的下标
del l[0]  # 删除第一个元素
l.pop(-1)  # 删除最后一个元素
l.remove(25)  # 删除第一个出现的该元素
print(l.count(1))  # 查看某元素个数
print(len(l))  # 查看元素总个数
l.clear()  # 清空列表
print(l)
