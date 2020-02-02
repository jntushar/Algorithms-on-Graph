# Uses python3
import sys
import queue


def extract_min(visited, dist):
    dist2 = dist[:]
    for i in visited:
        dist2[i] = 99999999
    return dist2.index(min(dist2))


def distance(adj, cost, s, t):
    queue = []
    queue.append(s)
    dist = [99999999] * len(adj)
    dist[s] = 0
    visited = []
    while queue:
        node = queue.pop(queue.index(extract_min(visited, dist)))
        for i, j in zip(adj[node], cost[node]):
            if i not in queue and i not in visited:
                queue.append(i)
            if dist[i] > dist[node] + j:
                dist[i] = dist[node] + j
        visited.append(node)
    return dist[t] if dist[t] != 99999999 else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
