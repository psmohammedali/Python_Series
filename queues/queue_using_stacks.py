class my_queue:
    def __init__(self):
        self.main_stack = []
        self.extra_stack = []
        self.length = 0

    def enqueue(self, data):
        self.main_stack.append(data)
        self.length +=1

    def dequeue(self):
        if self.length == 0:
            return -1
        while len(self.main_stack) !=0:
            self.extra_stack.append(self.main_stack.pop())
        removed_data = self.extra_stack.pop()
        while len(self.extra_stack) !=0:
            self.main_stack.append(self.extra_stack.pop())
        self.length -= 1

    def front(self):
        if self.length == 0:
            return -1
        while len(self.main_stack) != 1:
            self.extra_stack.append(self.main_stack.pop())
        front_data = self.main_stack[0]
        while len(self.extra_stack) !=0:
            self.main_stack.append(self.extra_stack.pop())
        return front_data

    def size(self):
        return self.length

    def isempty(self):
        return self.length == 0

obj = my_queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.dequeue()
print(obj.front())