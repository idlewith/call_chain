"""
把两两列表转换成相邻字典
"""

from pprint import pprint

a = "A"
b = "B"
c = "C"
d = "D"
e = "E"

abcd = [[a, b], [a, c], [b, d], [b, e], [c, d], [c, e], [d, e]]

adjacency_dict = {}
for up, down in abcd:
    adjacency_dict.setdefault(up, []).append(down)

pprint(adjacency_dict)
