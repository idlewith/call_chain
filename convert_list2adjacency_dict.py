"""
把两两列表转换成相邻字典, 相当于列出来每个节点后面的节点有哪些
"""

from pprint import pprint

a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
g = "G"
h = "H"

abcd = [[a, b], [a, c], [b, d], [b, e], [c, d], [c, e], [d, e], [g, h]]

adjacency_dict = {}
for up, down in abcd:
    adjacency_dict.setdefault(up, []).append(down)

pprint(adjacency_dict)
