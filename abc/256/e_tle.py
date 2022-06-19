# -*- coding: utf-8 -*-

import networkx as nx
import itertools
# import numpy as np


n = int(input())
# x_list = np.array([int(v) - 1 for v in input().split()])
# c_list = np.array([int(v) for v in input().split()])
x_list = [int(v) - 1 for v in input().split()]
c_list = [int(v) for v in input().split()]

# graph = [[] * n for _ in range(n)]
graph = nx.DiGraph()
# graph.add_nodes_from(range(n))

for i in range(n):
    x = x_list[i]
    c = c_list[i]
    # graph.add_edge(i, x, weight=c)
    graph.add_edge(i, x)
# print(graph.edges)  # [(0, 2), (1, 3), (2, 2)]

# network-x 何もわからん。色々試した。---
# print(graph.edges.data("weight"))  # [(0, 2, 1), (1, 3, 10), (2, 2, 100)]
# print(graph.edges)  # [(0, 2), (1, 3), (2, 2)]
# print(graph.nodes.data)
# print(graph.edges.data["weight"])

# is_scc = nx.is_strongly_connected(graph)

# if is_scc:
#     scc = nx.strongly_connected_components(graph)
#     print(next(scc))

# if nx.is_weakly_connected(graph):
# ---

# 弱連結成分（無向グラフにした時の連結成分）
wcc_itr = nx.weakly_connected_components(graph)
# inf = 10 ** 10
ans = 0

# copied_graph = graph.copy()
for wcc in wcc_itr:
    # 各連結成分は functional graph なので、サイクルを持つ。
    sub_graph = graph.subgraph(wcc)  # 元のグラフから連結成分のサブグラフをとってくる。
    # print("sub_graph:", sub_graph.edges)
    cycle_nodes = None  # サイクルを構成するノード
    try:
        cycle = nx.find_cycle(sub_graph)
        # print("cycle:", cycle)
        # cycle_nodes = np.array(cycle).flatten()
        # cycle_nodes = np.unique(cycle_nodes)
        cycle_nodes = list(itertools.chain.from_iterable(cycle))
        cycle_nodes = set(cycle_nodes)
        # print("cycle_nodes:", cycle_nodes)
    except nx.exception.NetworkXNoCycle:
        # サイクルが取れない場合は例外が出るのでキャッチして飛ばす。
        continue

    # サイクルを構成する頂点の中で最も小さい不満度を探す。
    # min_cost = np.min(c_list[cycle_nodes])
    min_cost = min([c_list[cn] for cn in cycle_nodes])
    ans += min_cost

    # nx.cycle_graph(wcc)
print(ans)
