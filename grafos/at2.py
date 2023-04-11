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
matrizInfo = np.ones(4)

def tipoGrafo(matriz):
    """
    Determina o tipo do grafo e carrega suas informaçoes em matrizInfo

    Parametros
    --------------------
    matriz  (Matriz de adjacencia do grafo)
    
    Retorna
    --------------------
    0   - Grafo simples
    1   - Grafo Dirigido
    20  - Multigrafo Simples
    21  - Multigrafo Dirigido
    30  - Pseudografo Simples
    31  - Pseudografo Dirigido
    """
    matriz = np.array(matriz)
    # checa se o grafo eh dirigido e se eh um multigrafo
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                # grafo eh dirigido
                matrizInfo[0] = 2
            if matriz[i][j] > 1 or matriz[j][i] > 1:
                # grafo eh um multigrafo
                matrizInfo[1] = 3

    # achar forma melhor de checar se existe algum numero diferente de 0
    if sum(matriz.diagonal()) != 0:
        matrizInfo[1] = 4

    # calcula quantidade de arestas pelo handshke's theorem
    if matrizInfo[0] == 1:
        matrizInfo[2] = matriz.sum() / 2
    else:
        matrizInfo[2] = matriz.sum()

    # calcula quantidade de vertices pelo tamanho da matriz
    matrizInfo[3] = len(matriz[0])
    

    # checa se o grafo eh simples
    if matrizInfo[0] == 1:
        # checa se eh multigrafo simples
        if matrizInfo[1] == 3:
            return 20
        # checa se eh Pseudografo simples
        elif matrizInfo[1] == 4:
            return 30
        # grafo eh apenas simples
        else:
            return 0
    # grafo eh dirigido
    else:
        # checa se eh multigrafo dirigido
        if matrizInfo[1] == 3:
            return 21
        # checa se eh Pseudografo dirigido
        elif matrizInfo[1] == 4:
            return 31
        # grafo eh dirigido
        else:
            return 1


    

def verificaAdjacencia(matriz, vi, vj):
    """
    Verifica se a adjacencia entre dois vertices existe

    Parametros
    ---------------------
    matriz  (Matriz de adjacencia do grafo)
    vi e vj (vertices a serem testados)

    Return
    ---------------------
    Boolean 
    """
    matriz = np.array(matriz)
    # Checa se os vertices vi e vj existem
    if matriz[vi].all() == -1:
        return 'Vertice vi nao existe na matriz'
    elif matriz[vj].all() == -1:
        return 'Vertice vj nao existe na matriz'

    # checa existencia da adjacencia      
    if matriz[vi][vj] >= 1 or matriz[vj][vi] >= 1:
        return True

    return False

def calcDensidade(matriz):
    """
    Calcula densidade do grafo 

    Informaçoes da matriz
    ----------------------
    matrizInfo[0] => 1 = Simples, 2 = Dirigido
    matrizInfo[1] => 3 = Multigrafo, 4 = Pseudografo
    matrizInfo[2] => |Vertices|
    matrizInfo[3] => |Arestas|

    Parametros
    ---------------------
    matriz  (Matriz de adjacencia do grafo)

    Retorna
    ---------------------
    valor da densidade (entre 0 e 1)

    """
    matriz = np.array(matriz)
    tipoGrafo(matriz)

    # checa se o grafo eh simples
    if matrizInfo[0] == 1:
        # densidade grafo simples
        densidade = (2 * matrizInfo[3]) / (matrizInfo[2] * (matrizInfo[2] - 1))
    else:
        # densidade grafo direcionado
        densidade = matrizInfo[3] / (matrizInfo[2] * (matrizInfo[2] - 1))
    
    return densidade

def insereAresta(matriz, vi, vj):
    """
    Insere aresta entre dois vertices (vi e vj)

    Parametros
    ----------------------
    matriz  (Matriz de adjacencia do grafo)
    vi e vj (vertices a serem conectados)

    Retorna
    ----------------------
    Sucesso:
       matriz atualizada em caso de sucesso
    Erro:
        'N tem esses vertices n parceir@' caso pelo menos um dos vertices nao existe
    
    """
    matriz = np.array(matriz)
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
def insereVertice(matriz):
    matriz = np.array(matriz)
   
    matriz = np.column_stack((matriz, np.zeros(len(matriz[0]))))
    matriz = np.row_stack((matriz, np.zeros(len(matriz[0]))))

    return matriz


def removeAresta(matriz, vi, vj):
    """
    Remove aresta entre dois vertices

    Parametros
    ---------------------
    matriz  (Matriz de adjacencia do grafo)
    vi e vj (vertices cuja aresta em comum sera removida)

    Retorna
    ---------------------
    Sucesso:
        matriz atualizada
    Erro:
        'Os vertices nao possuem arestas que os conectam' 
        'Tem esse vertice n fi' (caso o vertice nao exista na matriz)
    """
    matriz = np.array(matriz)
    try:
        if matriz[vi][vj] >= 1:
            matriz[vi][vj] -= 1
            matriz[vj][vi] -= 1
            return matriz
        else:
            return 'Os vertices nao possuem arestas que os conectam'
    except:
        return 'Tem esse vertice n fi'


def removeVertice(matriz, vi):
    """
    Remove vertice da matriz (altera todos os seus valores para -1)

    Parametros
    ----------------------
    matriz  (Matriz de adjacencia do grafo)
    vi      (vertice a ser removido)

    Retorna
    ----------------------
    Sucesso:
        matriz atualizada
    Erro:
        'Vertice nao existe na matriz'
    """
    matriz = np.array(matriz)
    try:
        matriz[vi] = -1
        # ver como muda valores coluna
        matriz[:, vi] = -1
        return matriz
    except:
        return 'Vertice nao existe na matriz'




