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

    def bfs(self):
        queue = []
        results = []
        current_node = self.root
        queue.append(current_node)
        while queue:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results


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

print("-----------------------  BFS -----------------------")
tree = BinarySearchTree()
tree.insert(10)
tree.insert(12)
tree.insert(13)
tree.insert(20)
print(tree.bfs())

print("-----------------------  DFS Pre Order -----------------------")
tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)
print(tree.dfs_pre_order())

print("-----------------------  DFS Post Order -----------------------")
tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)
print(tree.dfs_post_order())

print("-----------------------  DFS In Order -----------------------")
tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)
print(tree.dfs_in_order())
