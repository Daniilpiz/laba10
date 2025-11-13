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