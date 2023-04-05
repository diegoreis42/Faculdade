import numpy as np
import at1

"""
Informaçoes da matriz
----------------------
matrizInfo[0] => 1 = Simples, 2 = Dirigido
matrizInfo[1] => 3 = Multigrafo, 4 = Pseudografo
matrizInfo[2] => |Vertices|
matrizInfo[3] => |Arestas|
"""
matrizInfo = []


def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] >= 1 or matriz[vj][vi] >= 1:
        return True
    return False

def insereAresta(matriz, vi, vj):
    try:
        if vi == vj:
            matriz[vi][vj] += 1
        else:
            matriz[vi][vj] += 1
            matriz[vj][vi] += 1

        return matriz
    except:
        return 'N tem esses vertices n parceir@'


# Fazer isso aqui quando estiver com internet
def insereVertice(matriz, vi):
    add =  np.zeros((len(matriz[0])), dtype=int)
    matriz = np.r_[matriz, [add]]
    add =  np.zeros((len(matriz[:0])), dtype=int)
    matriz = np.column_stack((matriz, add))
    
    return matriz


def removeAresta(matriz, vi, vj):
    try:
        if matriz[vi][vj] >= 1:
            matriz[vi][vj] -= 1
            matriz[vj][vi] -= 1
            return matriz
        else:
            return 'Os vertices nao possuem arestas que os conectam'
    except:
        return 'Tem esse vertice n fi'


matrix = at1.createDefaultMatrix('ponte')

print(verificaAdjacencia(matrix, 1, 1))
print(insereAresta(matrix, 10, 10))
print(removeAresta(matrix, 1, 0))
