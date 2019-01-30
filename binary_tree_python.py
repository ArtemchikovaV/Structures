"""Binary tree structure"""

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BinaryTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        self.root = self._add(value, self.root)

    def _add(self, value, root):
        if root == None:
            root = TreeNode(value)
            return root
        if value < root.value:
            root.leftChild = self._add(value, root.leftChild)
        else:
            root.rightChild = self._add(value, root.rightChild)
        return root

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root == None:
            return False
        if root.value == value:
            return True

        if value < root.value:
            return self._search(root.leftChild, value)
        else:
            return self._search(root.rightChild, value)

    def max(self):
        node = self.root
        while node != None:
            if node.rightChild == None:
                return node.value
            else:
                node = node.rightChild

    def min(self):
        node = self.root
        while node != None:
            if node.leftChild == None:
               return node.value
            else:
                node = node.leftChild


tree = BinaryTree()
date = [4, 6, 7, 2, 3, 9, 0, 4, 6, 5]
for x in date:
    tree.add(x)
print(tree.min())
print(tree.max())
print(tree.search(5))
print(tree.search(1))