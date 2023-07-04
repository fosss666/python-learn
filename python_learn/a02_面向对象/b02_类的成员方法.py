class Student:
    name = None

    def say_hi(self, msg):
        print(f"我是{self.name},{msg}")


s = Student()
s.name = "周杰洛"
s.say_hi("我最帅")
