import sys
sys.setrecursionlimit(1000000)

def dfs(graph, visited, node_id):
    visited[node_id] = True
    print(node_id + 1, end=" ")

    for adj_id in graph[node_id]:
        if not visited[adj_id]:
            dfs(graph, visited, adj_id)
            print(node_id + 1, end=" ")


if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n-1):
        a, b = [int(v) - 1 for v in input().split()]
        graph[a].append(b)
        graph[b].append(a)

    for n_id in range(n):
        graph[n_id].sort()

    visited = [False] * n
    dfs(graph, visited, 0)

    print()
