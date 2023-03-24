import numpy as np
import sys


path = '/home/merlin/study/Faculdade/grafos/Instancias/' 


if __name__ == "__main__":
    """
     Arguments of the script

     Parameters
     ------------------
     [1]InstanceName, [2]InstanceID
    """
    InstanceName, InstanceID = str(sys.argv[1]), str(sys.argv[2])


def createDefaultMatrix(inst, id):
    """
    Read a text instance, transform it in a ndarray and return
    the ndarray

    Parameters
    -------------------
    inst (Name's Instance)
    id   (Id's Instance)
    """
    pathFile = path + inst + id + '.txt'

    with open(pathFile, 'rb') as f:
        nrows, ncols = [int(field) for field in f.readline().split()]
        data = np.genfromtxt(f, dtype='int32', max_rows=nrows)

    return data



def saveMatrixFile(InstanceName, data):
    """
    Print the name and size of the matrix, and save it in a file

    Parameters
    ------------------
    InstanceName (string)
    data (ndarray)
    """
    print('Salvando {} de formato {}' .format(InstanceName, data.shape))
    
    file = open('ans.txt', 'w')
    file.write(InstanceName + ' ' + str(data.shape[0]) + ' ' + str(data.shape[1]) + '\n')


# Executando codigo

data = createDefaultMatrix(InstanceName, InstanceID)

saveMatrixFile(InstanceName, data)
