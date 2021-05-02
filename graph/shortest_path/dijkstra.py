def dijkstra(nodes, distances):
    unvisited = {node: None for node in nodes}
    processed = {}
    current = 's'
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour in processed: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance

        processed[current] = currentDistance
        del unvisited[current]
        if not unvisited: return processed
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

nodes = ('s', 'a', 'b', 't')
distances = {
            's': {'a': 6, 'b': 2},
            'a': {'t': 1},
            'b': {'a': 3, 't': 5},
            't': {}
            }

print(dijkstra(nodes, distances)) # {'s': 0, 'b': 2, 'a': 5, 't': 6}