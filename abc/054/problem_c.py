def dfs(graph, visited, node_id):
    cnt = 0
    visited[node_id] = True
    if all(visited):
        visited[node_id] = False
        return 1

    for adj_id in graph[node_id]:
        if not visited[adj_id]:
            cnt = cnt + dfs(graph, visited, adj_id)

    visited[node_id] = False
    return cnt


if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = [int(v) - 1 for v in input().split()]
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    cnt = dfs(graph, visited, 0)
    print(cnt)
