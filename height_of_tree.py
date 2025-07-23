class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(self, root):
    if not root:
            return 0
        
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(4)



print(maxDepth([3,9,20,15,7])) 