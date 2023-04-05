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




matrix = at1.createDefaultMatrix('ponte')

print(verificaAdjacencia(matrix, 1, 1))

print(insereAresta(matrix, 10, 10))
