class GraphPathsFinder:
    def __init__(self, edge_list):
        """
        初始化图路径查找器。

        参数：
        - edge_list: 包含节点关系的列表，每个关系由两个节点组成。
        """
        self.edge_list = edge_list
        # 表示图的邻接字典，用于存储节点之间的关系。
        self.adjacency_dict = self.convert_to_adjacency_dict()
        # 起始节点列表
        self.start_nodes = self.find_start_nodes()
        # 结束节点列表
        self.end_nodes = self.find_end_nodes()

    def convert_to_adjacency_dict(self):
        """
        将节点列表转换为邻接字典。

        参数：
        - edge_list: 包含节点关系的列表，每个关系由两个节点组成。

        返回：
        - 表示图的邻接字典。
        """
        adjacency_dict = {}
        for node1, node2 in self.edge_list:
            # 将节点1添加到节点2的邻居列表中
            adjacency_dict.setdefault(node1, []).append(node2)

        return adjacency_dict

    def find_start_nodes(self):
        """
        找出图中的所有起始节点。

        返回：
        - 包含起始节点的列表。
        """
        potential_start_nodes = set(self.adjacency_dict.keys())
        for node, neighbors in self.adjacency_dict.items():
            # 起始节点是所有节点集合减去邻居集合的结果
            potential_start_nodes -= set(neighbors)

        return list(potential_start_nodes)

    def find_end_nodes(self):
        """
        找出图中的结束节点。

        返回：
        - 包含结束节点的列表。
        """
        potential_end_nodes = set()
        for node, neighbors in self.adjacency_dict.items():
            potential_end_nodes |= set(neighbors)

        # 结束节点是所有邻居集合减去节点集合的结果
        potential_end_nodes -= set(self.adjacency_dict.keys())

        return list(potential_end_nodes)

    def depth_first_search(self, node, current_path, all_paths):
        """
        深度优先搜索算法，递归查找所有可能的路径。

        参数：
        - node: 当前节点。
        - current_path: 当前路径。
        - all_paths: 存储所有路径的列表。
        """
        if node in self.end_nodes:
            # 如果当前节点是结束节点之一，则将当前路径添加到结果集中
            all_paths.append(current_path + [node])
            return

        # 如果当前节点不在图中，直接返回
        if node not in self.adjacency_dict:
            return

        # 对当前节点的邻居进行深度优先搜索
        for neighbor in self.adjacency_dict[node]:
            if neighbor not in current_path:
                self.depth_first_search(
                    neighbor,
                    current_path + [node],
                    all_paths,
                )

    def find_all_paths(self):
        """
        查找所有可能的路径。

        返回：
        - 所有可能的路径的列表。
        """
        all_paths = []
        for start_node in self.start_nodes:
            self.depth_first_search(
                start_node,
                [],
                all_paths,
            )

        return all_paths

    def generate_all_paths(self):
        """
        生成所有可能的路径。

        返回：
        - 所有可能的路径的列表。
        """
        all_paths = self.find_all_paths()
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
    graph_paths_finder = GraphPathsFinder(edge_list)
    all_paths = graph_paths_finder.generate_all_paths()

    for path in all_paths:
        print(path)


if __name__ == "__main__":
    main()
