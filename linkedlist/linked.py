class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    head = None
    tail = None
    while True:
        my_input = int(input())
        if my_input == -1:
            break
        cur_node = node(my_input)
        if head == None:
            head = cur_node
            tail = cur_node
        else:
            tail.next = cur_node
            tail = cur_node

    return head


def print_nodes(head):
    while head is not None:
        print(head.data)
        head = head.next


def print_ith_node(head, idx):
    count = -1
    while head is not None:
        count = count + 1
        if count == idx:
            print(head.data)
            return
        head = head.next

    print(None)
    return


def insert_ele_ith_node(head, idx, element):
    insert_node = node(element)
    # Inserting at the beginning of the linked list
    if idx == 0:
        insert_node.next = head
        return insert_node

    count = 0
    temp = head
    while temp.next is not None:
        if count == idx - 1:
            next_ref = temp.next
            temp.next = insert_node
            insert_node.next = next_ref
            return head
        count += 1
        temp = temp.next

    if count == idx -1:
        temp.next = insert_node
    return head


head = takeInput()
# print_nodes(head)

# print_ith_node(head, 3)
head = insert_ele_ith_node(head,2,9999)
print_nodes(head)