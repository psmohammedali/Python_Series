class father:
    def __init__(self):
        self.name = "father"
        print(self)

    def father_method(self):
        print("this is self", self.name)


class son(father):
    def __init__(self, ):
        self.name = "ali"
        super().__init__()

        pass


s = son()
print(s.name)
