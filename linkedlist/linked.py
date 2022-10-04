class node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = 0
for i in range(1,10):
    cur_node = node(i)
    if head == 0:
        # print("hae")
        head = cur_node
        continue
    temp = head
    while temp.next != None:
        print(temp)
        temp = temp.next
    temp.next = cur_node


temp = head

while temp != None:
    print(temp.data)
    temp = temp.next