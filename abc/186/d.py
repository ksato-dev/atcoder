# -*- coding: utf-8 -*-

n = int(input())
a_list = [int(v) for v in input().split()]
a_list.sort(reverse=True)

# 累積和
a_rs = [0] * (n + 1)
for i in range(1, n + 1):
    a_rs[i] = a_rs[i - 1] + a_list[i - 1]

# a_list が降順なら以下の計算が成立。
total_sum = 0
for i in range(n - 1):
    sum1 = a_list[i] * (n - (i + 1))
    sum2 = a_rs[n] - a_rs[i + 1]
    total_sum += abs(sum1 - sum2)

print(total_sum)
