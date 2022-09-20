class father:
    def __init__(self):
        self.name = "father"


class mother:
    def __init__(self, eye_color):
        self.name = "mohter"





class son(father, mother):
    def __init__(self,):
        self.name = "ali"
        super().__init__()

        pass


s1 = son()
print(s1.__dict__)



