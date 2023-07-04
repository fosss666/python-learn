class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"我叫{self.name}，年龄{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age < +other.age

    def __eq__(self, other):
        return (self.age == other.age) & (self.name == other.name)


s1 = Student("张三", 18)
s2 = Student("王柳", 20)
s3 = Student("王柳", 20)

print(s1)
print(s1 < s2)
print(s1 == s2)
print(s2 == s3)
