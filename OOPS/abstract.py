from abc import ABC, abstractmethod


class automobile(ABC):

    def __init__(self,wheels):
       self.no_wheels = wheels
       print("This is init from automobile")

    @abstractmethod
    def start(self):
        print("this is start from automobile", self.no_wheels)
        print((self))
        pass


class train(automobile):
    def __init__(self,wheels):
        super().__init__(wheels)
        self.no_wheels = wheels

        print("this is init from train")

    def train_start(self):
        print("Printing train started")

    def start(self):
       super().start()
       print("this is start from train")


t = train(52)
t.start()