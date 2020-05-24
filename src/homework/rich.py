import numpy as np


def to_nx_graph(rows):
    numNodes = len(rows)
    matrix = []
    for _list in rows:
        row = buildRow(_list, numNodes)
        matrix.append(row)
    matrix2 = np.array(matrix)
    return matrix2


def buildRow(_list, numNodes):
    # create base row
    baseRow = [0]
    while numNodes != 1:
        baseRow.append(0)
        numNodes = numNodes - 1
    for i in _list:
        baseRow[i] = 1
    return(baseRow)
