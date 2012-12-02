'''
Find the minimal path sum from the top left to the
bottom right by moving right and down.
'''

import csv
import networkx as nx


def main():
    matrix = []
    with open('src/matrix.txt', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            matrix.append([int(a) for a in row])

    G = nx.DiGraph()
    G.add_nodes_from([(i, j) for i in range(80) for j in range(8)])
    s = (-1, -1)  # supersource
    t = (80, 80)  # supersink
    G.add_nodes_from([s, t])  # supersource and supersink
    G.add_edge(s, (0, 0), weight=0)
    G.add_edge((79, 79), t, weight=matrix[-1][-1])
    for i in range(80):
        for j in range(80):
            w = matrix[i][j]
            if i < 79:  # down
                G.add_edge((i, j), (i + 1, j), weight=w)
            if j < 79:  # right
                G.add_edge((i, j), (i, j + 1), weight=w)

    return nx.single_source_dijkstra_path_length(G, source=s)[t]

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
