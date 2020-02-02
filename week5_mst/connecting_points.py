# Uses python3
import sys
import math


def dist(x1, y1, x2, y2):               # calculating the distance between two points
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def cal_weight(weight, adj, x, y, n):   # calculating weight of all the edges from a single point
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].append(j)
                weight[i].append(dist(x[i], y[i], x[j], y[j]))
            else:
                weight[i].append(0)


def minimum_distance(adj, weight, n):      # kruskal algorithm
    result = 0.
    MST = set()
    MST.add(0)
    while len(MST) != n:
        edges = set()
        for vertex in MST:
            for neighbour in adj[vertex]:
                if neighbour not in MST:
                    edges.add((vertex, neighbour))
        sorted_edges = sorted(edges, key=lambda x: weight[x[0]][x[1]])[0]
        MST.add(sorted_edges[1])
        result += weight[sorted_edges[0]][sorted_edges[1]]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    weight = [[] for _ in range(n)]
    adj = [[] for _ in range(n)]
    cal_weight(weight, adj, x, y, n)
    print("{0:.9f}".format(minimum_distance(adj, weight, n)))
