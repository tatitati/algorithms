#     A
# 	  /\
#    B  C
#   /   /\
#  D   E  F


# adjacency matrix
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs_iterative(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue = queue + graph[vertex]
    return visited

print("BFS iterative")
print(bfs_iterative(graph, 'A')) # A B C D E F


def dfs_iterative(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack = stack + graph[vertex]
    return visited

print("DFS iterative")
print(dfs_iterative(graph, 'A')) # A C F E B D


def dfs_recursive(graph, start, visited=[]):
    visited.append(start)
    for neighboor in graph[start]:
        dfs_recursive(graph, neighboor, visited)
    return visited

print("DFS recursive")
print(dfs_recursive(graph, 'A')) # A B D E F