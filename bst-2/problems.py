from queue import Queue


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def create_tree_level():
    user_input = int(input())
    if user_input == -1:
        return None
    my_queue = Queue()
    first_node = TreeNode(user_input)
    my_queue.put(first_node)
    while my_queue.qsize() != 0:
        curr_node = my_queue.get()
        # find left
        left_input = int(input(f"Enter the left value of node {curr_node.val}: "))
        right_input = int(input(f"Enter the right value of node {curr_node.val}: "))
        if left_input != -1:
            left_node = TreeNode(left_input)
            curr_node.left = left_node
            my_queue.put(left_node)
        if right_input != -1:
            right_node = TreeNode(right_input)
            curr_node.right = right_node
            my_queue.put(right_node)
    return first_node


def print_tree(root):
    if root is None:
        return
    my_queue = Queue()
    my_queue.put(root)
    while my_queue.qsize() != 0:
        current_node = my_queue.get()
        print(current_node.val, ": ", end=" ")
        if current_node.left is not None:
            my_queue.put(current_node.left)
            print("L", current_node.left.val, ",", end="")
        if current_node.right is not None:
            my_queue.put(current_node.right)
            print("R", current_node.right.val, end="")
        print()


root = create_tree_level()
print_tree(root)
