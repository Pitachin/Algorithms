""" The bellman ford algorithm for calculating single source shortest
paths - CLRS style """
graph = { 
    's' : {'t':6, 'y':7},
    't' : {'x':5, 'z':-4, 'y':8 },
    'y' : {'z':9, 'x':-3},
    'z' : {'x':7, 's': 2},
    'x' : {'t':-2}
}

INF = float('inf') # representation of infinity

dist = {}
predecessor = {} # to store the predecessor of each vertex in the path

def initialize_single_source(graph, s):
    for v in graph:
        dist[v] = INF
        predecessor[v] = None
    dist[s] = 0
    
def relax(graph, u, v):
    if dist[v] > dist[u] + graph[u][v]: # u is former vertex, v is latter vertex.
        dist[v] = dist[u] + graph[u][v]
        predecessor[v] = u

def bellman_ford(graph, s):
    initialize_single_source(graph, s)
    edges = [(u, v) for u in graph for v in graph[u].keys()] # list of edges, e.g. (u, v)
    number_vertices = len(graph)
    # Standard Bellman-Ford: relax all edges |V|-1 times.
    # Optimization: if one full pass makes no changes, we can stop early.
    for i in range(number_vertices-1):
        changed = False
        for (u, v) in edges:
            # before relaxing, record old distance to detect change
            old = dist.get(v, INF)
            relax(graph, u, v)
            if dist.get(v, INF) != old: # distance changed
                changed = True
        if not changed:
            break
    for (u, v) in edges:
        if dist[v] > dist[u] + graph[u][v]:
            return False # there exists a negative cycle
    return True

def get_distances(graph, s):
    if bellman_ford(graph, s):
        return dist
    return "Graph contains a negative cycle"

print(get_distances(graph, 's')) # fix error
