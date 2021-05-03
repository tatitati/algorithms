def dijkstra(nodes, graph):
    fromNode = 's'
    unvisited = nodes
    table = {}
    for node in nodes:
        table[node] = {"distance": None, "through": None}

    while(unvisited != []):
        fromNode = unvisited[0]
        for neighbour, distanceToNeighboor in graph[fromNode].items():
            if(table[neighbour]["distance"] is None):
                table[neighbour]["distance"] = distanceToNeighboor
                table[neighbour]["through"] = fromNode
            if(table[neighbour]["distance"] is not None):
                if distanceToNeighboor < table[neighbour]["distance"]: # this is called "relax" (we reduce the distance)
                    table[neighbour]["distance"] = distanceToNeighboor
                    table[neighbour]["through"] = fromNode
        unvisited.remove(fromNode)

    return table


nodes = ['s', 'a', 'b', 't']
graph = {
            's': {'a': 6, 'b': 2},
            'a': {'t': 1},
            'b': {'a': 3, 't': 5},
            't': {}
            }

print(dijkstra(nodes, graph))
# {
#   's': {'distance': None, 'through': None},
#   'a': {'distance': 3, 'through': 'b'},
#   'b': {'distance': 2, 'through': 's'},
#   't': {'distance': 1, 'through': 'a'}
# }
