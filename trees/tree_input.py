class tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    user_input = int(input("root data: " ))
    if user_input == -1:
        return None
    current_node = tree_node(user_input)
    left_node = take_input()
    right_node = take_input()
    current_node.left = left_node
    current_node.right = right_node
    return current_node
