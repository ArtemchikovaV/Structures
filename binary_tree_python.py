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

    def preOrder(self):
        result = []
        self._preOrder(self.root, result)
        return result

    def _preOrder(self, root, result):
        if root == None:
            return

        result.append(root.value)
        self._preOrder(root.leftChild, result)
        self._preOrder(root.rightChild, result)

    def inOrder(self):
        result = []
        self._inOrder(self.root, result)
        return result


    def _inOrder(self, root, result):
        if root == None:
            return

        self._inOrder(root.leftChild, result)
        result.append(root.value)
        self._inOrder(root.rightChild, result)


    def postOrder(self):
        result = []
        self._postOrder(self.root, result)
        return result

    def _postOrder(self, root, result):
        if root == None:
            return

        self._postOrder(root.leftChild, result)
        self._postOrder(root.rightChild, result)
        result.append(root.value)


tree = BinaryTree()
date = [4, 6, 7, 2, 3, 9, 0, 4, 6, 5]
for x in date:
    tree.add(x)

print(tree.preOrder())
print(tree.inOrder())
print(tree.postOrder())
print(tree.min())
print(tree.max())
print(tree.search(5))
print(tree.search(1))