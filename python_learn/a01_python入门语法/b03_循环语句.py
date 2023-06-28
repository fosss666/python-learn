import random

# 案例1 求1~100的和
# num = 1
# sum = 0;
# while num <= 100:
#     sum += num
#     num += 1
# print("1~100的和为：%d" % sum)
# 案例2 猜数字
# num = random.randint(1, 100)
# count = 1
# while True:
#     i = int(input(f"第{count}次猜："))
#     if i == num:
#         print("猜对啦")
#         break
#     else:
#         if i > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#     count += 1

# 案例3-九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i * j}\t", end='') #end=''的作用是不换行
#         j += 1
#     i += 1
#     print()
# 案例4-数数几个a
# name = "itheima is a brand of itcast"
# count = 0
# for c in name:
#     if c == "a":
#         count += 1
# print(count)
# 案例5-有几个偶数
# count = 0
# for num in range(1, 100):
#     if num % 2 == 0:
#         count += 1
# print("1到100（不含100本身）范围内，有%d个偶数" % count)

# 案例6-for循环打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}*{i}={j * i}\t", end='')
#     print()

# 综合案例-发工资
account = 10000
for i in range(1, 21):
    if account <= 0:
        print("工资发完了，下个月领取吧。")
        break
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}，绩效分{score}，低于5，不发工资，下一位。")
        continue
    else:
        account -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{account}元")
