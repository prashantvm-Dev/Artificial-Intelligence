# BFS Program

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = []
queue = ['A']

while queue:
    node = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for i in graph[node]:
            queue.append(i)
