from collections import deque


def bfs(node):
    queue = deque()
    visited = []
    queue += node
    while len(queue) != 0:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += graph[node]
            print(node, "-")


if __name__ == '__main__':
    graph = {}
    graph["A"] = ["B", "D"]
    graph["B"] = ["C", "D"]
    graph["C"] = ["F"]
    graph["D"] = ["E"]
    graph["E"] = ["C", "G"]
    graph["F"] = ["G"]
    graph["G"] = []

    bfs("A")


