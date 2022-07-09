# -*- coding :utf-8 -*-

import bisect

n, m, k = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]
b_list = [int(v) for v in input().split()]

a_rs_list = [0] * (n + 1)
b_rs_list = [0] * (m + 1)

for i in range(1, n + 1):
    a_rs_list[i] = a_rs_list[i - 1] + a_list[i - 1]

for i in range(1, m + 1):
    b_rs_list[i] = b_rs_list[i - 1] + b_list[i - 1]

max_book_num = 0
for i in range(n + 1):
    a_rs = a_rs_list[i]  # ０からの累積和を求める。
    limit_b_rs = k - a_rs

    j = 0
    found_b_rs_id = bisect.bisect_left(b_rs_list, limit_b_rs)
    if len(b_rs_list) <= found_b_rs_id:
        found_b_rs_id = found_b_rs_id - 1

    j = found_b_rs_id
    if b_rs_list[found_b_rs_id] <= limit_b_rs:
        j = found_b_rs_id
    else:
        # ある値より大きい時は右に１ずれるので、調整
        j = found_b_rs_id - 1

    a_num = i
    if k < a_rs_list[i] + b_rs_list[j]:
        continue

    book_num = a_num + j
    if max_book_num < book_num:
        max_book_num = book_num

print(max_book_num)
