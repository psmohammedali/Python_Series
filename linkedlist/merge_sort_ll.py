# Node Class Structure
class node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_ll(my_list):
    head = None
    tail = None
    for i in my_list:
        if i == -1:
            break
        cur_node = node(i)
        if tail is None:
            tail = cur_node
            head = cur_node
        else:
            tail.next = cur_node
            tail = cur_node
    return head


def print_ll(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


def middle_node(head):
    # if head is None or head.next is None:
    #     return head
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_ll(head1, head2):
    # if head1 is None and head2 is None:
    #     return None
    # if head1 is None:
    #     return head2
    # if head2 is None:
    #     return head1
    final_head = None
    final_tail = None
    temp1 = head1
    temp2 = head2
    while temp1 is not None and temp2 is not None:

        if temp1.val > temp2.val:
            cur_node = temp2
            temp2 = temp2.next
            cur_node.next = None
        else:
            cur_node = temp1
            temp1 = temp1.next
            cur_node.next = None

        if final_tail is None:
            final_tail = cur_node
            final_head = cur_node
        else:
            final_tail.next = cur_node
            final_tail = cur_node

    if temp1 is not None:
        final_tail.next = temp1
    if temp2 is not None:
        final_tail.next = temp2
    return final_head


def merge_sort(head):
    if head is None or head.next is None:
        return hstacks
        head

    mid_node = middle_node(head)
    head2 = mid_node.next
    mid_node.next = None
    ans1 = merge_sort(head)
    ans2 = merge_sort(head2)

    final_head = merge_ll(ans1, ans2)
    return final_head


# -1 in the list is the indication for the end of the linked list
if __name__ == "__main__":
    my_list = [1, 3, 5, 2, 2, 7, 5, -1]
    head = create_ll(my_list)
    print_ll(head)
    ans = merge_sort(head)
    print_ll(ans)
