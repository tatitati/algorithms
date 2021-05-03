# Like Dijkstra's shortest path algorithm, the Bellman-Ford algorithm is guaranteed to find the
# shortest path in a graph. Though it is slower than Dijkstra's algorithm, Bellman-Ford is capable
# of handling graphs that contain negative edge weights, so it is more versatile. It is worth noting
# that if there exists a negative cycle in the graph, then there is no shortest path. Going around the
# negative cycle an infinite number of times would continue to decrease the cost of the path (even
# though the path length is increasing). Because of this, Bellman-Ford can also detect negative cycles
# which is a useful feature.


INF = float("inf")

def bellman_ford(graph, nodes, src):
    dists = {node: INF for node in nodes}
    dists[src] = 0
    # table -> {'a': 0, 'b': inf, 'c': inf, 'd': inf, 'e': inf}


    # "Relax" iterations. Each node is processed N-1 times
    for _ in range(len(nodes) - 1):
        for node in graph:
            for neighboor, distanceToNeighboor in graph[node].items():
                if dists[node] == INF: continue
                if dists[node] + distanceToNeighboor < dists[neighboor]:
                    dists[neighboor] = dists[node] + distanceToNeighboor

    # check negative cycles
    for node in graph:
        for neighboor, distanceToNeighboor in graph[node].items():
            if dists[node] == INF: continue
            if dists[node] + distanceToNeighboor < dists[neighboor]:
                print("Graph contains negative weight cycle")
                return

    return dists


nodes = ["a", "b", "c", "d", "e"]
graph = {
    'a': {'b': -1, 'c': 4},
    'b': {'c': 3, 'd': 2, 'e': 2},
    'd': {'c': 5, 'b': 1},
    'e': {'d': -3}
}


print(bellman_ford(graph, nodes, "a"))
# {
#   'a': 0,
#   'b': -1,
#   'c': 2,
#   'd': -2,
#   'e': 1
# }