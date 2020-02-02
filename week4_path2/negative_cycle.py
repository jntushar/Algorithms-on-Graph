# Uses python3
import sys


def negative_cycle(adj, cost):
    dist = [9999] * len(adj)
    dist[0] = 0
    for _ in range(1, len(adj)):
        for node in range(len(adj)):
            for i, j in zip(adj[node], cost[node]):
                if dist[i] > dist[node] + j:
                    dist[i] = dist[node] + j

    for node in range(len(adj)):
        for i, j in zip(adj[node], cost[node]):
            if dist[i] > dist[node] + j:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
