from queue import Queue
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class BST_class:
    def __init__(self):
        self.__count = 0
        self.root = None

    def __helper_insert(self, root, val_node):
        if root is None:
            return val_node
        if root.val > val_node.val:
            left_subtree = self.__helper_insert(root.left, val_node)
            root.left = left_subtree
        else:
            right_subtree = self.__helper_insert(root.right, val_node)
            root.right = right_subtree

        return root

    def insert(self, val):
        val_node = TreeNode(val)
        self.root = self.__helper_insert(self.root , val_node)
        self.__count += 1

    def delete(self, val):
        pass

    def __helper_present(self, root, val):
        if root is None:
            return False
        if root.val == val:
            return True
        if root.val > val:
            left_subtree = self.__helper_present(root.left, val)
            return left_subtree
        else:
            right_subtree = self.__helper_present(root.right, val)
            return right_subtree

    def is_present(self, val):
        ans = self.__helper_present(self.root, val)
        return ans

    def size(self):
        return self.__count


    def __helper_print(self,root):
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




    def print(self):
        self.__helper_print(self.root)




tree1 = BST_class()
my_size = tree1.size()
tree1.insert(10)
tree1.insert(12)
tree1.insert(1)
tree1.insert(11)
tree1.insert(5)
tree1.insert(3)
tree1.print()
