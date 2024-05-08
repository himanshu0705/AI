graph={}
n_edges = int(input("Enter the number of edges : "))
print("Enter the Source and Destination : ")
for _ in range(n_edges):
    edge = input().split()
    source,destination = edge
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

def dfs(graph,visited,node):
    if node not in visited:
        visited.add(node)
        print(node)
        for neighbour in graph[node]:
            dfs(graph,visited,neighbour)

def bfs(graph,visited,node):
    queue = []
    visited.add(node)
    queue.append(node)
    while queue:
        current = queue.pop(0)
        print(current,end=" ")
        for neighbour in graph[current]:
            visited.add(neighbour)
            queue.append(neighbour)

print('\n')
print("Depth First Search")
visited_dfs = set()
dfs_start = input("Input the Starting node of dfs : ")
dfs(graph,visited_dfs,dfs_start)

print('\n')
print("Breadth First Search")
visited_bfs = set()
bfs_start = input("Input the Starting node of bfs : ")
bfs(graph,visited_bfs,bfs_start)