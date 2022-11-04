# class tree_node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def print_binary_tree(root):
#     if root is None:
#         return
#     if root.left:
#         print(f'root {root.data}: left {root.left.data}')
#     else:
#         print(f'root {root.data}: left {None}')
#     if root.right:
#         print(f'root {root.data}: right {root.right.data}')
#     else:
#         print(f'root {root.data}: right {None}')
#     print_binary_tree(root.left)
#     print_binary_tree(root.right)
#
#
# def take_input():
#     user_input = int(input("data:"))
#     if user_input == -1:
#         return None
#     current_node = tree_node(user_input)
#     print(f"Enter left node of {user_input}")
#     left_node = take_input()
#     print(f"Enter right node of {user_input}")
#     right_node = take_input()
#     current_node.left = left_node
#     current_node.right = right_node
#     return current_node
#
# def remove_leaf_nodes(root):
#     if root is None:
#         return None
#     if root.left is None and root.right is None:
#         return None
#     left_ans = remove_leaf_nodes(root.left)
#     righ_ans = remove_leaf_nodes(root.right)
#     root.left = left_ans
#     root.right = righ_ans
#     return root
#
#
#
# def no_of_nodes(root):
#     if root is None:
#         return 0
#     left_node = no_of_nodes(root.left)
#     right_node = no_of_nodes(root.right)
#     return 1+ left_node + right_node
#
#
# root = take_input()
# print_binary_tree(root)
# ans = no_of_nodes(root)
# print("ans; ",ans)
# remove_leaf_nodes(root)
# print(no_of_nodes(root))

try:
  a = int(input())
  b = int(input())
  result = a/b
  print(result)

except:
   print("We Catched an Error")

else:
   print("Hurray, We don't have any errors")

finally:
   print("I have reached the end of the line")