
import heapq

# Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3)],
    'C': [('A', 4), ('D', 1)],
    'D': [('B', 3), ('C', 1), ('E', 2)],
    'E': [('D', 2)]
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 2,
    'E': 0
}

def a_star(graph, heuristic, start, goal):
    open_list = []

    # f(start) = g(start) + h(start)
    heapq.heappush(open_list, (heuristic[start], start))

    # Cost from start
    g_cost = {start: 0}

    # Store parent node
    parent = {start: None}

    while open_list:
        f_current, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        # Explore neighbours
        for neighbour, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g

                # Calculate f(n) = g(n) + h(n)
                f_neighbour = new_g + heuristic[neighbour]

                heapq.heappush(
                    open_list, (f_neighbour, neighbour)
                )

                # Store parent
                parent[neighbour] = current

    return None, float("inf")


# Run A*
path, cost = a_star(graph, heuristic, 'A', 'E')

print("Shortest path:", path)
print("Total cost:", cost)
