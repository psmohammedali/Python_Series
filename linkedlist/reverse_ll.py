# Node Class Definition
class node:
    def __init__(self, data):
        self.val = data
        self.next = None


def create_ll(my_list):
    head = None
    tail = None
    for i in my_list:
        if i == -1:
            return head
        cur_node = node(i)
        if tail is None:
            head = cur_node
            tail = cur_node
        else:
            tail.next = cur_node
            tail = cur_node


def reverse_ll_iterative(head):
    final_head = None
    while head is not None:
        next_head = head.next
        head.next = final_head
        final_head = head
        head = next_head
    return final_head


def reverse_ll_recursive(head):
    if head is None: return None, None
    if head.next is None :return head, head
    small_head, small_tail = reverse_ll_recursive(head.next)
    head.next = None
    small_tail.next = head
    small_tail = head
    return small_head, small_tail

def reverse_ll_effective(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_ll_effective(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return small_head


def ll_print(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()


head = create_ll([1, 2, 3, 4, 6, -1])
ll_print(head)
head = reverse_ll_iterative(head)
ll_print(head)
head, tail = reverse_ll_recursive(head)
ll_print(head)
head = reverse_ll_effective(head)
ll_print(head)
# ll_print(head)
