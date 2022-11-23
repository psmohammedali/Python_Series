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


def take_input():
    user_input = int(input("data:"))
    if user_input == -1:
        return None
    current_node = tree_node(user_input)
    print(f"Enter left node of {user_input}")
    left_node = take_input()
    print(f"Enter right node of {user_input}")
    right_node = take_input()
    current_node.left = left_node
    current_node.right = right_node
    return current_node


def no_of_nodes(root):
    if root is None:
        return 0
    left_node = no_of_nodes(root.left)
    right_node = no_of_nodes(root.right)
    return left_node + right_node


def largest_node(root):
    if root is None:
        return 0
    left_largest = largest_node(root.left)
    right_largest = largest_node(root.right)
    return max(root.data, max(left_largest, right_largest))


def height_of_tree(root):
    if root is None:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    my_height = max(left_height, right_height) + 1
    return my_height


def no_of_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left_leaves = no_of_leaf_nodes(root.left)
    right_leaves = no_of_leaf_nodes(root.right)
    return left_leaves + right_leaves


def nodes_at_depth_k(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        print("///")
        return
    nodes_at_depth_k(root.left, k - 1)
    nodes_at_depth_k(root.right, k - 1)


def my_solution(root, targetSum):
    if root is None:
        return [[]]
    # Applies only for leaf node
    # if the left element is able be cancel targetSum to zero, then it's into consideration.
    if root.left is None and root.right is None:
        if targetSum - root.data == 0:
            return [[root.data]]
        else:
            return [[]]

    left_ans = pathSum(root.left, targetSum - root.data)
    right_ans = pathSum(root.right, targetSum - root.data)

    if len(left_ans[0]) > 0:
        for i in left_ans:
            i.append(root.data)
    if len(right_ans[0]) > 0:
        for i in right_ans:
            i.append(root.data)

    if len(right_ans[0]) == 0:
        return left_ans
    if len(left_ans[0]) == 0:
        return right_ans
    return left_ans + right_ans


def pathSum(root, targetSum):
    my_ans = my_solution(root, targetSum)
    print(my_ans)
    return [[]]


def bst_height(root):
    if root is None:
        return 0
    left_height = bst_height(root.left)
    right_height = bst_height(root.right)
    return 1 + max(left_height, right_height)


def is_bst(root):
    if root is None:
        return True
    left_height = bst_height(root.left)
    right_height = bst_height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    is_left_bst = is_bst(root.left)
    is_right_bst = is_bst(root.right)
    return is_left_bst and is_right_bst


def is_bst_better(root):
    if root is None:
        return 0, True
    left_height, left_bst = is_bst_better(root.left)
    right_height, right_bst = is_bst_better(root.right)
    if left_bst and right_bst:
        if abs(left_height - right_height) <= 1:
            return 1 + max(left_height, right_height), True

    return 1 + max(left_height, right_height), False


def diameter_tree(root):
    if root is None:
        return 0, 0
    left_height, left_max_diameter = diameter_tree(root.left)
    right_height, right_max_diameter = diameter_tree(root.right)

    my_height = max(left_height, right_height) + 1
    my_diameter = left_height + right_height
    if my_diameter >= left_max_diameter and my_diameter >= right_max_diameter:
        highest_diameter = my_diameter
    elif left_max_diameter > my_diameter and left_max_diameter > right_max_diameter:
        highest_diameter = left_max_diameter
    else:
        highest_diameter = right_max_diameter

    return my_height, highest_diameter


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
        left_val = int(input())
        right_val = int(input())
        if left_val != -1:
            left_node = tree_node(left_val)
            current_node.left = left_node
            my_queue.put(left_node)
        if right_val != -1:
            right_node = tree_node(right_val)
            current_node.right = right_node
            my_queue.put(right_node)
    return final_head


def create_tree_preorder_inorder(preorder_list, inorder_list):
    if len(preorder_list) == 0 and len(inorder_list) == 0:
        return None
    print("preorder_list: ",preorder_list)
    print("Inorder list: ",inorder_list)
    print()
    current_node = tree_node(preorder_list[0])

    my_root = preorder_list[0]

    in_order_root_index = inorder_list.index(my_root)
    in_order_left = inorder_list[0:in_order_root_index]
    in_order_right = inorder_list[in_order_root_index + 1:]

    len_left_in_order = len(in_order_left)
    pre_order_left = preorder_list[1:len_left_in_order+1]
    pre_order_right = preorder_list[len_left_in_order + 1:]

    left_subtree = create_tree_preorder_inorder(pre_order_left,in_order_left)
    right_subtree = create_tree_preorder_inorder(pre_order_right,in_order_right)

    current_node.left = left_subtree
    current_node.right = right_subtree
    return current_node


# root = level_order_input()
# print_binary_tree(root)
# print(largest_node(root))
# print(height_of_tree(root))
# ans = pathSum(root, 22)
# my_height , high_dia = diameter_tree(root)
# print(my_height)
# print(high_dia)

pre_order = [int(i) for i in input().split()]
in_order = [int(i) for i in input().split()]
root = create_tree_preorder_inorder(pre_order,in_order)
print_binary_tree(root)



