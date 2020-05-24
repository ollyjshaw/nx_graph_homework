import numpy as np


def to_nx_graph(rows):
    total_nodes = len(rows)
    array_of_arrays = [_transform(r, total_nodes) for r in rows]
    return np.array(array_of_arrays)


def _transform(row, total_nodes):
    arcs = []
    for i in range(total_nodes):
        arcs.append(1 if i in row else 0)
    return arcs
