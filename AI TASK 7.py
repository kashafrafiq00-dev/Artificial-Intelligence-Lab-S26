import heapq

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 3,
    'G': 0
}


def a_star(start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:

        current = heapq.heappop(open_list)[1]

        if current == goal:
            break

        for neighbor in graph[current]:

            new_cost = g_cost[current] + graph[current][neighbor]

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    path = []
    node = goal

    while node:
        path.append(node)
        node = parent[node]

    path.reverse()

    return path

start_node = 'A'
goal_node = 'G'

path = a_star(start_node, goal_node)

print("Shortest Path:", path)