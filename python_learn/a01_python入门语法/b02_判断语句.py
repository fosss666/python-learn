# 布尔类型
num_1 = 10
num_2 = 20
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(f"num_1比num_2大吗？{num_1 > num_2}")

# if语句
age = 18
if age >= 18:
    print(f"我成年了，今年{age}岁喽")
# 案例1
# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("您已成年，游玩需要补票10元。")
# else:
#     print("小孩子无需付费")
# print("祝您游玩愉快。")

# 案例2
num = 1
# i = int(input("请输入第一次猜想的数字："))
# if i == num:
#     print("猜对喽")
# else:
#     i = int(input("不对，再猜一次："))
#     if i == num:
#         print("猜对喽")
#     else:
#         i = int(input("不对，再猜最后一次："))
#         if i == num:
#             print("终于猜对喽")
#         else:
#             print("Sorry，全部猜错了，我想的是：%d" % num)


if int(input("请输入第一次猜想的数字：")) == num:
    print("猜对喽")
elif int(input("不对，再猜一次：")) == num:
    print("猜对喽")
elif int(input("不对，再猜最后一次：")) == num:
    print("终于猜对喽")
else:
    print("Sorry，全部猜错了，我想的是：%d" % num)
