def dfs(node):
    stack = []
    visited = []
    stack.append(node)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += graph[node]
            print(node, "-", end=" ")


if __name__ == '__main__':
    graph = {}
    graph["A"] = ["B", "D"]
    graph["B"] = ["C", "D"]
    graph["C"] = ["F"]
    graph["D"] = ["E"]
    graph["E"] = ["C", "G"]
    graph["F"] = ["G"]
    graph["G"] = []

    dfs("A")