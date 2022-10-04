class name:
    def __init__(self):
        self.n = "Ali"
    def calling_name(self):
        print("my name is ",self.n)

class student(name):
    def __init__(self):
        super().__init__()
        self.age = 23

    def this_is_calling(self):
        print("this is student fuctnion")


stu1 = student()
stu1.calling_name()
