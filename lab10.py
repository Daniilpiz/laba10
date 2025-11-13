from func import *
from generatives import *

def verts(G):
    start_0 = int(input("Введите вершину, с которой начать"))

    distances_0 = bfsd(G_0, start_0)
    print(distances_0)
    print(diametr(G_0))
    perif(G_0)
    print(radius(G_0))
    centr(G_0)


if __name__ =="__main__":
    
    G_0 = generator_smezh(4)
    verts(G_0)

    start_1 = int(input("Введите вершину, с которой начать"))
    G = generate_adjacency_matrix_neor(4, density=0.3,)
    verts(G)

    start_2 = int(input("Введите вершину, с которой начать"))
    G_1 = generate_adjacency_matrix_or(4, density=0.6,)
    verts(G_1)