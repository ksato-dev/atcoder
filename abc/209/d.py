
import queue

n, q = [int(v) for v in input().split()]
m = n - 1
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = [int(v) for v in input().split()]
    a = a - 1
    b = b - 1
    graph[a].append(b)
    graph[b].append(a)

# create tree (root := 0) ---
dist = [-1] * n
todo = queue.Queue()
todo.put(0)
dist[0] = 0

while not todo.empty():
    curr_node = todo.get()

    for adj_node in graph[curr_node]:
        if dist[adj_node] != -1:
            continue
        dist[adj_node] = dist[curr_node] + 1
        todo.put(adj_node)
# --- create tree (root := 0)

# ans_list = list()
for i in range(q):
    c, d = [int(v) for v in input().split()]
    c = c - 1
    d = d - 1
    dist_bw_cd = dist[c] + dist[d]
    if dist_bw_cd % 2:
        print("Road")
        # ans = "Road"
    else:
        print("Town")
        # ans = "Town"
    # ans_list.append(ans)

# for ans in ans_list:
#     print(ans)
