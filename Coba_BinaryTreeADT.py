class BinarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert(node.right, data)

    def find(self, data):
        return self._find(self.root, data)

    def _find(self, node, data):
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self._find(node.left, data)
        else:
            return self._find(node.right, data)

# Contoh penggunaan
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)

node = bst.find(15)
if node:
    print(f'Node found: {node.data}')
else:
    print('Node not found')
