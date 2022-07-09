# -*- coding: utf-8 -*-

h, w, n = [int(v) for v in input().split()]

a_list = [None] * n
b_list = [None] * n

for i in range(n):
    a, b = [int(v) for v in input().split()]
    a_list[i] = a
    b_list[i] = b

sorted_a_list = sorted(set(a_list))
sorted_b_list = sorted(set(b_list))

coord_comp_a_dict = {v: i + 1 for i, v in enumerate(sorted_a_list)}
coord_comp_b_dict = {v: i + 1 for i, v in enumerate(sorted_b_list)}

for a, b in zip(a_list, b_list):
    ans_a_id = coord_comp_a_dict[a]
    ans_b_id = coord_comp_b_dict[b]
    print(ans_a_id, ans_b_id)
