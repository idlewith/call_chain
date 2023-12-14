"""
用两两节点的列表画图
"""

from graphviz import Digraph

# Given list
abcd = [
    ["A", "B"],
    ["A", "C"],
    ["B", "D"],
    ["B", "E"],
    ["C", "D"],
    ["C", "E"],
    ["D", "E"],
    ["G", "H"],
]

# Create a directed graph
graph = Digraph("CallChain")

# Add nodes and edges to the graph
for pair in abcd:
    graph.node(str(pair[0]))
    graph.node(str(pair[1]))
    graph.edge(str(pair[0]), str(pair[1]))

# Render the graph (choose a format: pdf, png, svg, etc.)
graph.render("call_chain_graph", format="png", cleanup=True)

# Display the rendered graph (use an image viewer or open the file)
graph.view("call_chain_graph")
