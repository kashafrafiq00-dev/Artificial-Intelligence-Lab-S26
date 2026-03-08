# BFS without Queue & without Node

print("BFS without Queue & without Node")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []
bfs_list = ['A']

while bfs_list:
    node = bfs_list.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        bfs_list = bfs_list + graph[node]

# BFS with Queue & Node

print("\n\nBFS with Queue & Node")

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def bfs_with_queue(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node.value, end=" ")
            visited.add(node)

            for child in node.children:
                queue.append(child)

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

A.children = [B, C]
B.children = [D, E]
C.children = [F, G]

bfs_with_queue(A)