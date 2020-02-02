# Uses python3
import sys
from collections import deque


def number_of_components(adj):
    queue = deque()
    visited = []
    result = check = 0
    while check < len(adj):
        if check not in visited:
            queue.append(check)
            while len(queue) != 0:
                node = queue.popleft()
                if node not in visited:
                    visited.append(node)
                    queue += adj[node]
            result += 1
        check += 1
    return result


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
    print(number_of_components(adj))
