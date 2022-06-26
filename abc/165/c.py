# -*- coding :utf-8 -*-

def dfs(n_id, n, m, a_list, pre_a, q_table, ans_list):

    # 最後まで来たら A が一通り揃っている。
    if n_id == n:
        ans = 0
        for query in q_table:
            a, b, c, d = query
            if c == a_list[b - 1] - a_list[a - 1]:
                ans += d
        ans_list.append(ans)
        return

    for i in range(pre_a, m + 1):
        next_a = i
        a_list[n_id] = next_a
        dfs(n_id + 1, n, m, a_list, next_a, q_table, ans_list)


n, m, q = [int(v) for v in input().split()]
q_table = [None] * q
for i in range(q):
    q_table[i] = [int(v) for v in input().split()]

a_list = [0] * n
ans_list = list()

dfs(0, n, m, a_list, 1, q_table, ans_list)

print(max(ans_list))