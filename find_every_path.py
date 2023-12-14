"""
深度优先算法 DFS 找到每条路径
"""


def find_all_paths(graph, start_nodes, end_nodes):
    def dfs(node, path):
        if node in end_nodes:
            paths.append(path + [node])
            return
        if node not in graph:
            return
        for neighbor in graph[node]:
            if neighbor not in path:
                dfs(neighbor, path + [node])

    paths = []
    for start_node in start_nodes:
        dfs(start_node, [])

    return paths


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["D", "E"],
        "D": ["E"],
        "G": ["H"],
    }
    start_nodes = ["A", "G"]
    end_nodes = ["H", "E"]

    result_paths = find_all_paths(graph, start_nodes, end_nodes)

    print("All paths between start and end nodes:")
    for path in result_paths:
        print(path)


if __name__ == "__main__":
    main()
