from queue import Queue

class Generic_Tree:
    def __init__(self, data):
        self.val = data
        self.child_list = []



def print_tree(root):
    if root is None:
        return
    print(root.val,end = ": ")
    for i in range(len(root.child_list)):
        print(root.child_list[i].val, end= ", ")
    print()

    for i in range(len(root.child_list)):
        print_tree(root.child_list[i])

def take_input():
    user_input = int(input("Root Data: "))
    if user_input == -1:
        return None
    curr_node = Generic_Tree(user_input)
    while True:
        child = take_input()
        if child is None:
            break
        curr_node.child_list.append(child)
    return

def take_input_better():
    user_input = int(input("Root Data: "))
    if user_input == -1:
        return None
    cur_node = Generic_Tree(user_input)
    children = int(input(f"Enter the num of childrens for {cur_node.val}: "))
    for i in range(children):
        print(f"Data of {i} child of {cur_node.val}")
        child = take_input_better()
        cur_node.child_list.append(child)

    return cur_node


def count_node(root):
    if root is None:
        return 0
    if len(root.child_list) == 0:
        return 1
    count = 1
    for i in root.child_list:
        subtree_count = count_node(i)
        count = count + subtree_count
    return count


def level_wise():
    user_input = int(input("Root Data: "))
    if user_input == -1:
        return None
    my_queue = Queue()
    head_node = Generic_Tree(user_input)
    my_queue.put(head_node)
    while my_queue.qsize() != 0:
        cur_node = my_queue.get()
        while True:
            child_input = int(input(f"Enter the children of {cur_node.val}: "))
            if child_input == -1:
                break
            child_node = Generic_Tree(child_input)
            cur_node.child_list.append(child_node)
            my_queue.put(child_node)
    return head_node


def level_wise_for():
    user_input = int(input("Root Data: "))
    if user_input == -1:
        return None
    my_queue = Queue()
    head_node = Generic_Tree(user_input)
    my_queue.put(head_node)
    while my_queue.qsize() != 0:
        cur_node = my_queue.get()
        no_of_children = int(input(f"Enter the no of children for {cur_node.val}: "))
        for i in range(no_of_children):
            child_input = int(input(f"Enter the children of {cur_node.val}: "))
            child_node = Generic_Tree(child_input)
            cur_node.child_list.append(child_node)
            my_queue.put(child_node)
    return head_node




root1 = Generic_Tree(0)
child1 = Generic_Tree(1)
child2 = Generic_Tree(2)
child3 = Generic_Tree(3)
child4 = Generic_Tree(4)
child5 = Generic_Tree(5)
child6 = Generic_Tree(6)
child7 = Generic_Tree(7)
child8 = Generic_Tree(8)
root1.child_list.append(child1)
root1.child_list.append(child2)
root1.child_list.append(child3)
root1.child_list.append(child4)

child2.child_list.append(child5)
child2.child_list.append(child6)
child2.child_list.append(child7)
child4.child_list.append(child8)

root = level_wise_for()
print_tree(root)
print(count_node(root))
