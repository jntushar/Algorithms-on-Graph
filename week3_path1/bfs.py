# Uses python3
import sys


def distance(adj, s, t):
   queue = []
   queue.append(s)
   prev = [999] * len(adj)
   prev[s] = 0
   while queue:
        node = queue.pop(0)
        for i in adj[node]:
            if prev[i] == 999:
                queue.append(i)
                prev[i] = prev[node] + 1
   if prev[t] == 999:
       return -1
   else:
       return prev[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
