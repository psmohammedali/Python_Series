class stack_using_list:
    # Constructor
    def __init__(self):
        self._my_list = []
        self._list_length = 0

    def push(self, data):
        self._my_list.append(data)
        self._list_length += 1

    def pop(self):
        if self.length == 0:
            return -1
        self._list_length -= 1
        idx = self._list_length - 1
        return self._my_list.pop(idx)

    def top(self):
        if self._list_length == 0:
            return -1
        return self._my_list[self._list_length-1]

    def is_empty(self):
        return self._list_length == 0

    def length(self):
        return self._list_length

# End result
stack = stack_using_list()

# Push operation  -  1
stack.push(12)
stack.push(13)

stack.push(14)
stack.push(15)
stack.push(16)
stack.push(17)

# pop Operation  -  2
pop1 = stack.pop()
pop2 = stack.pop()
print(pop1)
print(pop2)
# top Operation  -  3
top1 = stack.top()
print(top1)
# length Operation   -  4
length1 = stack.length()
print(length1)
# isEmpty Operation  -  5
empty1 = stack.is_empty()
print(empty1)
