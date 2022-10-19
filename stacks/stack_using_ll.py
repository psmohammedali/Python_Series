class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack_using_ll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
        cur_node = node(data)
        cur_node.next = self.head
        self.head = cur_node
        self.length += 1

    def top(self):
        if self.length == 0:
            return -1
        return self.tail.data

    def isempty(self):
        return self.length == 0

    def ll_length(self):
        return self.length

    def pop(self):
        if self.length == 0:
            return -1
        removed_node = self.head.data
        self.head = self.head.next
        self.length -=1
        return removed_node


stack = stack_using_ll()
stack.push(11)
stack.push(12)
stack.push(13)
stack.push(14)
stack.push(15)
while stack.isempty() is False:
    print(stack.pop())
