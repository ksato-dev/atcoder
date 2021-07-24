# ref: https://qiita.com/enbi/items/245c974fb6e62a8e238c
import sys
sys.setrecursionlimit(500*500)


def dfs(all_grp_ids, grp_id, graph, node_id, pre_id, is_not_cycle):
    all_grp_ids[node_id] = grp_id

    for adj_node_id in graph[node_id]:
        # whether is cycle?
        if all_grp_ids[adj_node_id] >= 0:
            if pre_id != -1 and pre_id != adj_node_id:
                is_not_cycle[adj_node_id] = False
            continue
        dfs(all_grp_ids, grp_id, graph, adj_node_id, node_id, is_not_cycle)


if __name__ == "__main__":
    n, m = [int(value) for value in input().split()]

    graph = [[] for _ in range(n+1)]
    all_grp_ids = [-1 for _ in range(n+1)]

    for _ in range(m):
        u, v = [int(value) for value in input().split()]
        graph[u].append(v)
        graph[v].append(u)

    # print(graph[1:])

    grp_id = 0
    tree_grp_ids = list()
    for node_id in range(1, n+1):
        if all_grp_ids[node_id] >= 0:
            continue

        if graph[node_id]:
            is_not_cycle = [True] * (n + 1)
            dfs(all_grp_ids, grp_id, graph, node_id, -1, is_not_cycle)
            if False in is_not_cycle:
                pass
            else:
                tree_grp_ids.append(grp_id)
        else:
            tree_grp_ids.append(grp_id)
            all_grp_ids[node_id] = grp_id
        grp_id = grp_id + 1

    print(len(tree_grp_ids))
