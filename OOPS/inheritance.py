class shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.__is_filled = is_filled

    # getters and setters
    def get_is_filled(self):
        return self.__is_filled

    def print(self):
        print(self.color)
        print(self.__is_filled)


class rectangle(shape):
    def __init__(self, color, is_filled, length, breadth):
        super().__init__(color, is_filled)
        self.length = length
        self.breath = breadth

    def print_details(self):
        super().print()

        # print(self.length)
        # print(self.breath)



r1 = rectangle("green", True, 5, 6)
# print(r1.__dict__)
r1.print_details()
