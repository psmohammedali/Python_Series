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


root = take_input()
print_binary_tree(root)
# print(largest_node(root))
# print(height_of_tree(root))
ans = pathSum(root,22)
print(ans)