import sys


def floydWarshall(cost, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
    return cost


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    cost = [[0]*n for _ in range(n)]
    for ((a, b), w) in edges:
        cost[a - 1][b - 1] = w
    for i in range(n):
        for j in range(n):
            if i != j and cost[i][j] == 0:
                cost[i][j] = 999999
    print(floydWarshall(cost, n))




