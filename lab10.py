from collections import deque
import numpy as np
import random as rd

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
        print(v)
        for i in range(len(G)):
            if G[v][i]>0 and dist[i]==-1:
                q.append(i)
                dist[i] = dist[v] + G[v][i]
    return dist


print(bfsd(generate_adjacency_matrix_neor(4, density=0.3,), 0))

print(bfsd(generate_adjacency_matrix_or(4, density=0.6,), 0))
