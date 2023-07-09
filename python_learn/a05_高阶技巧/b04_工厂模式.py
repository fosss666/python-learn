"""    
    @author: fosss
    Date: 2023/7/9
    Time: 14:33
    Description:
"""


class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:
    def get_person(self, p_type):
        if p_type == "w":
            return Worker()
        elif p_type == "s":
            return Student()
        else:
            return Teacher()


factory = PersonFactory()
worker = factory.get_person("w")
student = factory.get_person("s")
teacher = factory.get_person("t")
