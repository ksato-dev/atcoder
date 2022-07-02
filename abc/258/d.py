# -*- coding: utf-8 -*-


n, x = [int(v) for v in input().split()]

a_list = list()
b_list = list()
b_min_list = list()  # ある要素までの最小値をもたせる。

b_min = 10 ** 20
for i in range(n):
    a, b = [int(v) for v in input().split()]
    a_list.append(a)
    b_list.append(b)
    if b_min > b:
        b_min = b

    b_min_list.append(b_min)

# 累積和
a_rs = [0]*(n+1)
for i in range(1, n+1):
    a_rs[i] = a_rs[i-1] + a_list[i-1]

b_rs = [0]*(n+1)
for i in range(1, n+1):
    b_rs[i] = b_rs[i-1] + b_list[i-1]

total_sum = [0] * n
for i in range(n):
    a = a_list[i]
    b = b_list[i]
    b_min = b_min_list[i]
    total_sum[i] += (a_rs[i + 1] - a_rs[0]) + (b_rs[i + 1] - b_rs[0])
    total_sum[i] += (x - i - 1) * b_min

print(min(total_sum))
