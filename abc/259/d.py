# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(1000000000)


def dfs(graph, visited, node_id, tgt_id):
    visited[node_id] = True
    if node_id == tgt_id:
        print("Yes")
        exit()

    for adj_id in graph[node_id]:
        if not visited[adj_id]:

            dfs(graph, visited, adj_id, tgt_id)

# def dfs(graph, visited, node_id, tgt_id):
#     visited[node_id] = True
#     if node_id == tgt_id:
#         return True

#     for adj_id in graph[node_id]:
#         if visited[adj_id]:
#             continue
#         if dfs(graph, visited, adj_id, tgt_id):
#             return True
#     return False


n = int(input())
sx, sy, tx, ty = [int(v) for v in input().split()]

xyr_list = [None] * n
for i in range(n):
    x, y, r = [int(v) for v in input().split()]
    xyr_list[i] = (x, y, r)

circle_graph = [list() for _ in range(n)]
start_circle_id = None
tgt_circle_id = None
for i in range(n):
    x1, y1, r1 = xyr_list[i]
    sd2 = (x1 - sx) ** 2 + (y1 - sy) ** 2
    td2 = (x1 - tx) ** 2 + (y1 - ty) ** 2
    if sd2 == r1 ** 2:
        start_circle_id = i

    if td2 == r1 ** 2:
        tgt_circle_id = i

    for j in range(i + 1, n):
        x2, y2, r2 = xyr_list[j]
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2

        # どちらかの円がもう一方の内部にあるケース
        if d2 < (r1 - r2) ** 2:
            continue

        # どちらかの円がもう一方の外部にあるケース
        if d2 > (r1 + r2) ** 2:
            continue

        circle_graph[i].append(j)
        circle_graph[j].append(i)

visited = [False] * n
dfs(circle_graph, visited, start_circle_id, tgt_circle_id)
print("No")
