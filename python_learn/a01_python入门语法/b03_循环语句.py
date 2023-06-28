import random

# 案例1 求1~100的和
num = 1
sum = 0;
while num <= 100:
    sum += num
    num += 1
print("1~100的和为：%d" % sum)
# 案例2 猜数字
num = random.randint(1, 100)
count = 1
while True:
    i = int(input(f"第{count}次猜："))
    if i == num:
        print("猜对啦")
        break
    else:
        if i > num:
            print("猜大了")
        else:
            print("猜小了")
    count += 1
