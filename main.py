"""
完整版本：从自定义的每两两节点，根据深度优先算法，找出每天路径
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


def find_start_nodes(graph):
    # Find potential start node(s)
    potential_start_nodes = set(graph.keys())
    for node, neighbors in graph.items():
        potential_start_nodes -= set(neighbors)

    return list(potential_start_nodes)


def find_end_nodes(graph):
    # Find potential end node(s)
    potential_end_nodes = set()
    for node, neighbors in graph.items():
        potential_end_nodes |= set(neighbors)
    potential_end_nodes -= set(graph.keys())

    return list(potential_end_nodes)


def convert2adjacency(node_list):
    adjacency_dict = {}
    for up, down in node_list:
        adjacency_dict.setdefault(up, []).append(down)
    return adjacency_dict


def gen_all_paths(node_list):
    graph = convert2adjacency(node_list)
    start_nodes = find_start_nodes(graph)
    end_nodes = find_end_nodes(graph)
    all_paths = find_all_paths(graph, start_nodes, end_nodes)
    return all_paths


def main():
    node_list = [
        ["A", "B"],
        ["A", "C"],
        ["B", "D"],
        ["B", "E"],
        ["C", "D"],
        ["C", "E"],
        ["D", "E"],
        ["G", "H"],
    ]
    all_paths = gen_all_paths(node_list)
    for path in all_paths:
        print(path)


if __name__ == "__main__":
    main()
