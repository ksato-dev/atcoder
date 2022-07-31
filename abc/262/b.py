# -*- coding: utf-8 -*-


def main():
    n, m = [int(v) for v in input().split()]
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = [int(v) for v in input().split()]
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    ans = 0
    for a in range(n):
        for b in range(a + 1, n):
            # if a == b:
            #     continue
                
            connected_b = False
            for adj_a_id in graph[a]:
                if b == adj_a_id:
                    connected_b = True

            if not connected_b:
                continue

            # # ====
            # set_graph_ab = set(graph[a] + graph[b])
            # print(a, b, graph[a], graph[b], set_graph_ab)
            # # ====

            for c in range(b + 1, n):
                if a == c:
                    continue

                for adj_b_id in graph[b]:
                    if c == adj_b_id:
                        for adj_c_id in graph[c]:
                            if a == adj_c_id:
                                ans += 1
                
    print(ans)

    
if __name__ == "__main__":
    main()
