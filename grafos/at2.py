import numpy as np

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




