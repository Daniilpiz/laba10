from collections import deque

def bfsd(G, v):
    q = deque()
    q.append(v)
    dist = [-1]*len(G)

    dist[v] = 0

    while q:
        v = q.pop()
        # print(v)
        for i in range(len(G)):
            if G[v][i]>0 and dist[i]==-1:
                q.append(i)
                dist[i] = dist[v] + G[v][i]


    return dist


def ecentrice(distances, vertex):
    # print(f"эксцентриситет для вершины {vertex} равен {max(distances)}")
    return max(distances)

def diametr(G):
    diam = []
    for vertex in range(len(G)):
        diam.append(ecentrice(bfsd(G, vertex), vertex))

    return max(diam)
# print(bfsd(generate_adjacency_matrix_neor(4, density=0.3,), 1), ecentrice(bfsd(generate_adjacency_matrix_neor(4, density=0.3,), 1), 1))

# print(bfsd(generate_adjacency_matrix_or(4, density=0.6,), 2), ecentrice(bfsd(generate_adjacency_matrix_or(4, density=0.6,), 2), 2))

def perif(G):
    for vertex in range(len(G)):
        if ecentrice(bfsd(G, vertex), vertex) == diametr(G):
            print(f"вершина {vertex} периферийная")


def radius(G):
    rad = []
    for vertex in range(len(G)):
        rad.append(ecentrice(bfsd(G, vertex), vertex))

    return min(rad) if rad else print("граф плохой")

def centr(G):
    for vertex in range(len(G)):
        if ecentrice(bfsd(G, vertex), vertex) == radius(G):
            print(f"вершина {vertex} центральная")