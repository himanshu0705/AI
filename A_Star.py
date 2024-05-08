Graph = {
    'A' : [('B',2), ('E',3)],
    'B' : [('C',1), ('G',9)],
    'C' : [],
    'D' : [('G',1)],
    'E' : [('D',6)]
}

def a_star(start_node, stop_node):
    open = set([start_node])
    close = set()
    g = {start_node:0}
    parents = {start_node:start_node}

    while open:
        current_node = min(open, key=lambda x: g[x] + heuristic(x))
        
        if current_node == stop_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start_node)
            path.reverse()
            print('Path Found : ',path)
            return path
        
        open.remove(current_node)
        close.add(current_node)

        for neighbour, weight in get_neighbour(current_node):
            if neighbour in close:
                continue
            tentative_g = g[current_node] + weight

            if neighbour not in open or tentative_g < g[neighbour]:
                g[neighbour] = tentative_g
                parents[neighbour] = current_node
                open.add(neighbour)

    print("Path not found")
    return None

def heuristic(node):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(node, float('inf'))

def get_neighbour(node):
    return Graph.get(node, [])

a_star('A','G')