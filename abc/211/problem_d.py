from queue import Queue


def dfs(seen, todo, graph, start_id, tgt_id, dist, cnt):
    todo.put(1)
    dist[start_id] = 0
    seen[start_id] = True
    cnt[start_id] = 1
    # end_flag = False
    while not todo.empty():
        visited_id = todo.get()
        for adj_id in graph[visited_id]:
            if dist[adj_id] is not None:
                if dist[adj_id] == dist[visited_id] + 1:
                    cnt[adj_id] = cnt[adj_id] + cnt[visited_id]
                    cnt[adj_id] = cnt[adj_id] % (10**9+7)
                continue
            else:
                dist[adj_id] = dist[visited_id] + 1
                cnt[adj_id] = cnt[visited_id]
                # if next_id == tgt_id:
                #     dists_until_tgt.append(dist[next_id])
                todo.put(adj_id)


if __name__ == "__main__":
    n, m = [int(value) for value in input().split()]
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = [int(value) for value in input().split()]
        graph[a].append(b)
        graph[b].append(a)

    seen = [False] * (n + 1)
    todo = Queue()
    dist = [None] * (n + 1)
    cnt = [0] * (n + 1)

    dfs(seen, todo, graph, 1, n, dist, cnt)
    # dist_1_to_n = dist[n]
    print(dist)
    print(cnt)

    if cnt[n] > 0:
        print(cnt[n])
    else:
        print(0)
