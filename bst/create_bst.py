import sys
from queue import Queue


class tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_binary_tree(root):
    if root is None:
        return
    if root.left:
        print(f'root {root.data}: left {root.left.data}')
    else:
        print(f'root {root.data}: left {None}')
    if root.right:
        print(f'root {root.data}: right {root.right.data}')
    else:
        print(f'root {root.data}: right {None}')
    print_binary_tree(root.left)
    print_binary_tree(root.right)


def level_order_input():
    my_queue = Queue()
    user_input = int(input())
    if user_input == -1:
        return None
    node = tree_node(user_input)
    my_queue.put(node)
    final_head = node
    final_tail = node
    while my_queue.qsize() != 0:
        current_node = my_queue.get()

        left_val = int(input(f'Enter the left value of {current_node.data}:'))
        right_val = int(input(f'Enter the right value of {current_node.data}:'))
        if left_val != -1:
            left_node = tree_node(left_val)
            current_node.left = left_node
            my_queue.put(left_node)
        if right_val != -1:
            right_node = tree_node(right_val)
            current_node.right = right_node
            my_queue.put(right_node)
    return final_head


def max_node_val(root):
    if root is None:
        return -1
    left_max = max_node_val(root.left)
    right_max = max_node_val(root.right)
    return max(root.data, left_max, right_max)


def min_node_val(root):
    if root is None:
        return 100000
    left_min = min_node_val(root.left)
    right_min = min_node_val(root.right)
    return min(root.data, left_min, right_min)


def validate_binary_search_tree(root):
    if root is None:
        return True

    left_subtree_max = max_node_val(root.left)
    right_subtree_min = min_node_val(root.right)
    if not (left_subtree_max < root.data <= right_subtree_min):
        print(left_subtree_max, " ", root.data, " ", right_subtree_min)
        return False
    is_leftsubtree_bst = validate_binary_search_tree(root.left)
    is_rightsubtree_bst = validate_binary_search_tree(root.right)
    return is_leftsubtree_bst and is_rightsubtree_bst


def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)


def brute_force_diameter(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    my_diameter = left_height + right_height

    left_diameter = brute_force_diameter(root.left)
    right_diameter = brute_force_diameter(root.right)
    return max(left_diameter, right_diameter, my_diameter)


# HOPE - YES
def bst_better(root):
    if root is None:
        return 1 * sys.maxsize, -1 * sys.maxsize, True
    left_min, left_max, is_left_bst = bst_better(root.left)
    right_min, right_max, is_right_bst = bst_better(root.right)
    my_min = min(left_min, right_min, root.data)
    my_max = max(left_max, right_max, root.data)
    is_bst = False
    if is_left_bst and is_right_bst:
        if left_max < root.data <= right_min:
            is_bst = True
    print(my_min, " ", my_max, " ", is_bst)
    return my_min, my_max, is_bst


def is_bst_range(root,start,end):
    if root is None:
        return True
    if start <= root.data <= end:
        is_left_bst = is_bst_range(root.left, start,root.data-1)
        is_right_bst = is_bst_range(root.right,root.data,end)
        return is_left_bst and is_right_bst
    return False





#
root = level_order_input()
# # ans = validate_binary_search_tree(root)
# dia = brute_force_diameter(root)
# print(dia)

# my_min, my_max, is_bst = bst_better(root)
is_bst = is_bst_range(root,-1*sys.maxsize,sys.maxsize)
print(is_bst)

