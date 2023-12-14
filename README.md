# call chain

- [draw_graph.py](draw_graph.py) 用两两节点的列表画图，用来验证生成到路径是否正确
- 
- [convert_list2adjacency_dict.py](convert_list2adjacency_dict.py) 把两两列表转换成相邻字典, 相当于列出来每个节点后面的节点有哪些

- [find_start_end_node_from_graph.py](find_start_end_node_from_graph.py) 找到相邻字典的开始、结束节点

- [find_every_path.py](find_every_path.py) 深度优先算法 DFS 找到每条路径

- [main.py](main.py) 主脚本，两两节点列表到最后输出到每条路径