from func import *
from generatives import *


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