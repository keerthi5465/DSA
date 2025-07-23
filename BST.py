from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Sol:

    def insert(root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = Sol.insert(root.left, key)
        else:
            root.right = Sol.insert(root.right, key)
        return root

    def BFS(root):
        if not root:
            return
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            print(node.key, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


nodes = [50, 15, 62, 5, 20, 58, 91, 3, 8, 39, 60, 24]
root = None
for n in nodes:
    root = Sol.insert(root, n)

print("BFS (Level Order Traversal) of BST:")
Sol.BFS(root)
