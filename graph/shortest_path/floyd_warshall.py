# The Floyd-Warshall algorithm is a shortest path algorithm for graphs. Like the Bellman-Ford algorithm or
# the Dijkstra's algorithm, it computes the shortest path in a graph. However, Bellman-Ford and Dijkstra are
# both single-source, shortest-path algorithms. This means they only compute the shortest path from a single source.
# Floyd-Warshall, on the other hand, computes the shortest distances between every pair of vertices in the input graph.

INF = float("inf")


def floydWarshall(graph,n): #n=no. of vertex
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )
    return dist


graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

print(floydWarshall(graph, 4))
# [
#   [0, 5, 8, 9],
#   [inf, 0, 3, 4],
#   [inf, inf, 0, 1],
#   [inf, inf, inf, 0]
# ]