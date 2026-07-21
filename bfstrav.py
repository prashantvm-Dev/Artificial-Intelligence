from collections import deque
#Function Traversal
def bfs(graph,start):
    visited=set()
    queue=deque()
    visited.add(start)
    queue.append(start)
    print("BFS Traversal")
    while queue:
        node=queue.popleft()
        print(node,end="")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
#Graph Representation
graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
bfs(graph,'A')
