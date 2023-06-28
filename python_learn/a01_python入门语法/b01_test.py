# print("hello world")
666
# 单行注释

"""
多行注释
"""
# 使用type()查看数据类型
"""
t1 = 1
t2 = 1.0
t3 = "lalala"
print(type(t1))
print(type(t2))
print(type(t3))
"""
# 数据类型转换
"""
t1 = float(11)
print(t1)
print(type(t1))

t2 = str(11)
print(type(t2))

t3 = int("11")
print(type(t3))
"""

# 运算符
print("4/2=", 4 / 2)
print("2/3=", 2 / 3)
print("9整除2=", 9 // 2)
print("4指数2=", 4 ** 2)

# 字符串拼接 字符串不能直接用+和整型等拼接在一起，这点和java不一样
num = 1
# 错误写法 print("数字是："+ num)
print("数字是：", num)

# 字符串格式化-占位符
name = "张三"
age = 18
score = 99.555
# message = "我叫%s，今年%s岁了，考了%s分" % (name, age, score)
message = "我叫%s，今年%d岁了，考了%f分" % (name, age, score)
print(message)
# 数字的精度控制 m.n  m限制宽度（小于原宽度则不生效） n控制精度（四舍五入）
message = "我叫%s，今年%5d岁了，考了%.2f分" % (name, age, score)
print(message)
# 字符串格式化-快速格式化  字符串前面用f标记
print(f"我叫{name}，今年{age}岁了，考了{score}分")
# 对表达式进行格式化
print("1*1=%s" % (1 * 1))
print(f"1*2={1 * 2}")
print("字符串的数据类型：%s" % type(""))
