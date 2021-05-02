#     A
# 	  /\
#    B  C
#   /   /\
#  D   E  F


graph = {
    'A': set(['B', 'C']),
    'B': set(['D']),
    'C': set(['E', 'F']),
    'D': set([]),
    'E': set([]),
    'F': set([])
}


def bfs_iterative(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print("BFS iterative")
print(bfs_iterative(graph, 'A')) # A, B, C, D, E, F



def dfs_iterative(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print("DFS iterative")
print(dfs_iterative(graph, 'A')) # A, B, D, C, E, F



def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited

print("DFS recursive")
print(dfs_recursive(graph, 'A')) # A, B, D, C, E, F