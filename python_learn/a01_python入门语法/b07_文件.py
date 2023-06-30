# 文件读取操作-单词计数
# f = open("E:/fo的python学习\python_learn/a01_python入门语法/word.txt", "r", encoding="utf-8")
# a = f.readlines()
# print(a)
# count = 0
#
# for b in a:
#     c = b.split(" ")
#     for d in c:
#         if d == "itheima":
#             count += 1
#
# print(count)
# f.close()
# with open-自动关闭文件
with open("E:/fo的python学习\python_learn/a01_python入门语法/word.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
    print(a)
    count = 0

    for b in a:
        c = b.split(" ")
        for d in c:
            if d == "itheima":
                count += 1

    print(count)