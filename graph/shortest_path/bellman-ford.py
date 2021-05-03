INF = float("inf")

def bellman_ford(graph, nodes, src):
    dist = {node: INF for node in nodes}
    dist[src] = 0
    iterations = len(nodes) - 1

    # iterations
    for _ in range(iterations):
        for s, d, w in graph:
            if dist[s] != INF and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w

    # Step 3: detect negative cycle
    # if value changes then we have a negative cycle in the graph and we cannot find the shortest distances
    for s, d, w in graph:
        if dist[s] != INF and dist[s] + w < dist[d]:
            print("Graph contains negative weight cycle")
            return

    # No negative weight cycle found
    return dist


nodes = ["a", "b", "c", "d", "e"]
graph = [
    # s, d, w
    ["a", "b", -1],
    ["a", "c", 4],
    ["b", "c", 3],
    ["b", "d", 2],
    ["b", "e", 2],
    ["d", "c", 5],
    ["d", "b", 1],
    ["e", "d", -3]
]

print(bellman_ford(graph, nodes, "a"))
# {
#   'a': 0,
#   'b': -1,
#   'c': 2,
#   'd': -2,
#   'e': 1
# }