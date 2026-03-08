class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_stack(start):
    stack = [start]
    visited = set()

    print("\nDFS using Stack:")

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node.value, end=" ")
            visited.add(node)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)


def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

dfs_stack(root)

print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)