"""
完整版本：从自定义的每两两节点，根据深度优先算法，找出每天路径
"""


def find_all_paths(adjacency_dict, start_nodes, end_nodes):
    """
    从自定义的每两两节点，根据深度优先算法，找出所有可能路径。

    参数：
    - adjacency_dict: 表示图的邻接字典，用于存储节点之间的关系。
    - start_nodes: 包含可能的起始节点的列表。
    - end_nodes: 包含可能的结束节点的列表。

    返回：
    - 所有可能的路径的列表。
    """

    def depth_first_search(node, current_path):
        # 如果当前节点是结束节点之一，则将当前路径添加到结果集中
        if node in end_nodes:
            all_paths.append(current_path + [node])
            return

        # 如果当前节点不在图中，直接返回
        if node not in adjacency_dict:
            return

        # 对当前节点的邻居进行深度优先搜索
        for neighbor in adjacency_dict[node]:
            if neighbor not in current_path:
                depth_first_search(neighbor, current_path + [node])

    all_paths = []
    for start_node in start_nodes:
        depth_first_search(start_node, [])

    return all_paths


def find_start_nodes(adjacency_dict):
    """
    找出图中的所有起始节点。

    参数：
    - adjacency_dict: 表示图的邻接字典，用于存储节点之间的关系。

    返回：
    - 包含起始节点的列表。
    """
    # 所有节点的集合
    potential_start_nodes = set(adjacency_dict.keys())
    for node, neighbors in adjacency_dict.items():
        # 起始节点是所有节点集合减去邻居集合的结果
        potential_start_nodes -= set(neighbors)

    start_nodes = list(potential_start_nodes)
    return start_nodes


def find_end_nodes(adjacency_dict):
    """
    找出图中的结束节点。

    参数：
    - adjacency_dict: 表示图的邻接字典，用于存储节点之间的关系。

    返回：
    - 包含结束节点的列表。
    """
    # 所有节点的邻居的集合
    potential_end_nodes = set()
    for node, neighbors in adjacency_dict.items():
        potential_end_nodes |= set(neighbors)

    # 结束节点是所有邻居集合减去节点集合的结果
    # 比如E是最后一个节点，这个时候生成的adjacency_dict就没有E节点，
    # 所以减去所有key，剩下的就是结束节点
    potential_end_nodes -= set(adjacency_dict.keys())

    end_nodes = list(potential_end_nodes)
    return end_nodes


def convert_to_adjacency_dict(edge_list):
    """
    将节点列表转换为邻接字典。

    参数：
    - edge_list: 包含节点关系的列表，每个关系由两个节点组成。

    返回：
    - 表示图的邻接字典。
    """
    adjacency_dict = {}
    for node1, node2 in edge_list:
        # 将节点1添加到节点2的邻居列表中
        adjacency_dict.setdefault(node1, []).append(node2)

    return adjacency_dict


def generate_all_paths(edge_list):
    """
    生成所有可能的路径。

    参数：
    - edge_list: 包含节点关系的列表，每个关系由两个节点组成。

    返回：
    - 所有可能的路径的列表。
    """
    adjacency_dict = convert_to_adjacency_dict(edge_list)
    start_nodes = find_start_nodes(adjacency_dict)
    end_nodes = find_end_nodes(adjacency_dict)
    all_paths = find_all_paths(adjacency_dict, start_nodes, end_nodes)

    return all_paths


def main():
    edge_list = [
        ["A", "B"],
        ["A", "C"],
        ["B", "D"],
        ["B", "E"],
        ["C", "D"],
        ["C", "E"],
        ["D", "E"],
        ["G", "H"],
    ]
    all_paths = generate_all_paths(edge_list)
    for path in all_paths:
        print(path)


if __name__ == "__main__":
    main()
