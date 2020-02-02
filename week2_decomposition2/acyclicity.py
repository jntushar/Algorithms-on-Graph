# Uses python3

import sys


def acyclic(adj):
    stack = []
    visited = []
    check = step = 0
    while check < len(adj):
        stack.append(check)
        if len(adj[check]) == 0:
            check += 1
            continue
        while len(stack) != 0:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack += adj[node]
                step += 1
            if node == check and step > 1:
                return 1
        stack =[]
        visited = []
        step = 0
        check += 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
