class node:
    def __init__(self, data):
        self.val = data
        self.next = None


def reverseBetween(head, m, n):
    if not head:
        return None

    left, right = head, head
    stop = False

    def recurseAndReverse(right, m, n):
        nonlocal left, stop
        if n == 1:
            print(right.val)
            return

        right = right.next
        print('right', right.val)

        if m > 1:
            left = left.next
            print('left',left.val)


        recurseAndReverse(right, m - 1, n - 1)
        print('first',right.val)

        if left == right or right.next == left:
            stop = True

        if not stop:
            left.val, right.val = right.val, left.val
            left = left.next

    recurseAndReverse(right, m, n)
    return head


def ll_print(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()



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


head = create_ll([1, 2, 3, 4, 5,6,7,-1])
ll_print(head)
reverseBetween(head, 3,6)
ll_print(head)

