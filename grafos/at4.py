import numpy as np
import at2


def warshall(m):

    """
    Devolve a matriz de acessibilidade da matriz m
    utilizando o algoritmo de warshall

    Entradas
    ----------------
    matriz de adjacencias -> nd.array
    numero de vertices    -> int
    
    Saida
    ----------------
    matriz de acessibilidade -> nd.array
    """
    m = np.array(m)
    r = m.copy()
    n = len(r[0])
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if r[i][j] == 1 or (r[i][k] == 1 and r[k][j] == 1):
                    r[i][j] = 1
                else:
                    r[i][j] = r[i][j]
    return r

def caminhoEuleriano(g):
    """
    Checa se se o grafo possui caminho euleriano 
    utilizando os teoremas de euler

    Entrada
    ----------------
    matriz de adjacencias -> nd.array
    numero de vertices    -> int

    Saida
    ----------------
    Boolean
    """
    g = np.array(g)
    n = len(g[0])

    total, i = 0, 0
    while (total <= 2) and (i < n):
        grau = g[i].sum()
        if grau % 2 != 0:
            total += 1
        i += 1
    if total > 2 :
        return False
    else:
        return True


