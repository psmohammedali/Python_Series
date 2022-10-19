class my_queue:
    def __init__(self):
        self.my_list = []
        self.length = 0
        self.front_index = 0

    def enqueue(self, data):
        self.my_list.append(data)
        self.length += 1


    def dequeue(self):
        if self.length == 0:
            print("queue is empty")
            return
        # Queue is not empty
        removed_front_val = self.my_list[self.front_index]
        self.front_index +=1
        self.length -=1
        return removed_front_val

    def front(self):
        if self.length == 0:
            print("queue is empty")
            return
        # Queue is not empty
        return self.my_list[self.front_index]

    def size(self):
        return self.length

    def isempty(self):
        return self.length == 0

obj = my_queue()
obj.enqueue(11)
obj.enqueue(12)
obj.enqueue(13)
print(obj.front())
obj.dequeue()
print(obj.front())
obj.dequeue()
print(obj.front())
obj.dequeue()
print(obj.front())
obj.enqueue(19)
print(obj.front())
print(obj.size())
