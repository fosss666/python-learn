class Student:
    # name = None
    # age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("对象被创建")


s = Student("张三", 18)
print(s.name, s.age)
