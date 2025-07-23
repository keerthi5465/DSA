class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def nodes(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return nodes(root.left) + nodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(nodes(root)) 