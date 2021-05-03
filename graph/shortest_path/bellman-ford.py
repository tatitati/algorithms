# Print the solution
def print_solution(dist, V):
    print("Vertex Distance from Source")
    for i in range(V):
        print("{0}\t\t{1}".format(i, dist[i]))

def bellman_ford(graph, V, src):
    dist = [float("Inf")] * V
    dist[src] = 0

    # iterations
    for _ in range(V - 1):
        for s, d, w in graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w

    # Step 3: detect negative cycle
    # if value changes then we have a negative cycle in the graph
    # and we cannot find the shortest distances
    for s, d, w in graph:
        if dist[s] != float("Inf") and dist[s] + w < dist[d]:
            print("Graph contains negative weight cycle")
            return

    # No negative weight cycle found!
    # Print the distance and predecessor array
    print_solution(dist, V)


V = 5
graph = [
    # s, d, w
    [0, 1, -1],
    [0, 2, 4],
    [1, 2, 3],
    [1, 3, 2],
    [1, 4, 2],
    [3, 2, 5],
    [3, 1, 1],
    [4, 3, -3]
]

bellman_ford(graph, V, 0)