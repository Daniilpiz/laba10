from collections import deque
import numpy as np
import random as rd



def generator_smezh(razm):
    matr_sm = np.matrix(np.array([abs(rd.randint(-1000, 1000))%2 for _ in range(razm) for _ in range(razm)]).reshape(razm, razm))

    for i in range(razm):
        matr_sm[i, i] = 0
        for j in range(razm):
            if i<=j:
                matr_sm[i,j] = matr_sm[j, i]

    print(matr_sm)
    return matr_sm.tolist()

def generate_adjacency_matrix_neor(n, density=0.3, weight_range=(0, 100)):
    matrix = np.array([[0 for _ in range(n)] for _ in range(n)]).reshape(n, n)
    
    for i in range(n):
        for j in range(n):
            if i != j:  # без петель
                if rd.random() < density:
                    weight = rd.randint(weight_range[0], weight_range[1])
                    matrix[i][j] = weight
                    matrix[j][i] = weight
    print(matrix)
    return matrix.tolist()


def generate_adjacency_matrix_or(n, density=0.3, weight_range=(0, 100)):
    matrix = np.array([[0 for _ in range(n)] for _ in range(n)]).reshape(n, n)
    
    for i in range(n):
        for j in range(n):
            if i != j:  # без петель
                if rd.random() < density:
                    weight = rd.randint(weight_range[0], weight_range[1])
                    matrix[i][j] = weight
    print(matrix)
    return matrix.tolist()



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



if __name__ =="__main__":
    start_0 = int(input("Введите вершину, с которой начать"))
    G_0 = generator_smezh(4)
    distances_0 = bfsd(G_0, start_0)
    print(distances_0)
    print(diametr(G_0))
    perif(G_0)
    print(radius(G_0))
    centr(G_0)

    start_1 = int(input("Введите вершину, с которой начать"))
    G = generate_adjacency_matrix_neor(4, density=0.3,)
    distances_1 = bfsd(G, start_1)
    print(distances_1)
    print(diametr(G))
    perif(G)
    print(radius(G))
    centr(G)

    start_2 = int(input("Введите вершину, с которой начать"))
    G_1 = generate_adjacency_matrix_or(4, density=0.6,)
    distances_2 = bfsd(G_1, start_2)
    print(distances_2)
    print(diametr(G_1))
    perif(G_1)
    print(radius(G_1))
    print(centr(G_1))