class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    @staticmethod
    def min_value_node(current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


print("-------------------------- insert ops --------------------------")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(8)
print(bst.root.value)
print(bst.root.right.value)
print(bst.root.left.value)
print("------------------------------- contains ops -----------------------")
print(bst.contains(10))
print(bst.contains(8))
print(bst.contains(77))
print("---------------------------- mim ops ---------------------------------")
print(bst.min_value_node(bst.root).value)
bst.insert(6)
print(bst.min_value_node(bst.root).value)
bst.insert(7)
print(bst.min_value_node(bst.root).value)
bst.insert(2)
print(bst.min_value_node(bst.root).value)
print(bst.min_value_node(bst.root.left).value)