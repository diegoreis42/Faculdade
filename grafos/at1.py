import numpy as np


def createDefaultMatrix(inst, id):
    """
    Read a text instance, transform it in a ndarray and return
    the ndarray

    Parameters
    -------------------
    inst (Name's Instance)
    id   (Id's Instance)
    """
    path = '/home/merlin/study/Faculdade/grafos/Instancias/' + inst + id + '.txt'

    with open(path, 'rb') as f:
        nrows, ncols = [int(field) for field in f.readline().split()]
        data = np.genfromtxt(f, dtype='int32', max_rows=nrows)

    return data


data = createDefaultMatrix('teste', '1')
print(data)
