class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.key)
        preorder(root.left)
        preorder(root.right)
postorder = [10, 9, 23, 22, 27, 25, 15, 50, 95, 60, 40, 29]
root = None
for val in postorder:
    root = insert(root, val)
inorder(root)
preorder(root)
