INF = float("inf")

def bellman_ford(graph, nodes, src):
    dists = {node: INF for node in nodes}
    dists[src] = 0
    # table -> {'a': 0, 'b': inf, 'c': inf, 'd': inf, 'e': inf}


    # "Relax" iterations. Each node is processed N-1 times
    for _ in range(len(nodes) - 1):
        for node in graph:
            for neighboor, distanceToNeighboor in graph[node].items():
                if dists[node] + distanceToNeighboor < dists[neighboor] and dists[node] != INF:
                    dists[neighboor] = dists[node] + distanceToNeighboor

    # check negative cycles
    for node in graph:
        for neighboor, distanceToNeighboor in graph[node].items():
            if dists[node] + distanceToNeighboor < dists[neighboor] and dists[node] != INF:
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