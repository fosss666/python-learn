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
# with open("E:/fo的python学习\python_learn/a01_python入门语法/word.txt", "r", encoding="utf-8") as f:
#     a = f.readlines()
#     print(a)
#     count = 0
#
#     for b in a:
#         c = b.split(" ")
#         for d in c:
#             if d == "itheima":
#                 count += 1
#
#     print(count)

# 写操作,没有该文件则自动创建，每次写的内容会将原文件中的内容替换掉
# f = open("E:/fo的python学习\python_learn/a01_python入门语法/write.txt", "w", encoding="utf-8")
# f.write("Hello World!!")
# # f.flush()
# f.close()

# 追加写
f = open("E:/fo的python学习\python_learn/a01_python入门语法/write.txt", "a", encoding="utf-8")
f.write("河马")
f.write("\n河马")
f.close()
