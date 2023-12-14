"""
找到相邻字典的开始、结束节点
"""

def find_start_and_end_nodes(graph):
    # Find potential start node(s)
    potential_start_nodes = set(graph.keys())
    for node, neighbors in graph.items():
        potential_start_nodes -= set(neighbors)

    # Find potential end node(s)
    potential_end_nodes = set()
    for node, neighbors in graph.items():
        potential_end_nodes |= set(neighbors)

    potential_end_nodes -= set(graph.keys())

    return list(potential_start_nodes), list(potential_end_nodes)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["D", "E"],
    "D": ["E"],
    # 'E': []
}


# graph = {
#     "1": ["2", "5"],
#     "2": ["3", "4"]
# }


start_nodes, end_nodes = find_start_and_end_nodes(graph)

print("Start node(s):", start_nodes)
print("End node(s):", end_nodes)
