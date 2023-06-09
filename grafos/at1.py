import numpy as np
import sys




if __name__ == "__main__":
    """
     Arguments of the script

     Parameters
     ------------------
     [1]InstanceName
    """
    InstanceName = str(sys.argv[1])


def createDefaultMatrix(inst):
    """
    Read a text instance, transform it in a ndarray and return
    the ndarray

    Parameters
    -------------------
    inst (Name's Instance)

    Return
    -------------------
    data (ndarray do arquivo lido)
    """
    PATH = '../grafos/Instancias/' 

    pathFile = PATH + inst + '.txt'

    with open(pathFile, 'rb') as f:
        data = np.genfromtxt(f, dtype='int32')

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






