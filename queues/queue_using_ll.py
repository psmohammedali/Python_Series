class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue_ll:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def enqueue(self,data):
        cur_node= node(data)
        if self.head is None:
            self.head = cur_node
            self.tail = cur_node
        else:
            self.tail.next = cur_node
            self.tail = cur_node
        self.length +=1

    def dequeue(self):
        if self.head is None:
            return -1
        front_val = self.head.data
        self.head = self.head.next
        self.length -=1
        return front_val

    def size(self):
        if self.head is None:
            return -1
        return self.length

    def front(self):
        if self.head is None:
            return -1
        return self.head.data

    def isEmpty(self):
        return self.length == 0


obj = queue_ll()
obj.enqueue(12)
obj.enqueue(14)
obj.enqueue(16)
print(obj.front())
print(obj.dequeue())
print(obj.size())
print(obj.front())
print(obj.dequeue())
print(obj.front())
print(obj.dequeue())
print(obj.size())
print(obj.front())
print(obj.dequeue())
obj.enqueue(12)
print(obj.front())

