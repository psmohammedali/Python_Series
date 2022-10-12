class node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = node

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        print(self.head)

my_obj = LinkedList()
my_obj.print()