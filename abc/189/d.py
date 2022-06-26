# -*- coding: utf-8 -*-

n = int(input())

s_list = list()
for i in range(n):
    s = input()
    s_list.append(s)

# dp[i] := i 個の x (x_0 ~ x_i-1) を使って y_i を True にできる数
dp = [0] * (n + 1)
dp[0] = 1  # x_0 = True のときのみ

for i in range(1, n+1):
    s = s_list[i - 1]

    if s == "AND":
        # AND なら絶対に y_i-1 と x が True で無いといけない。
        dp[i] = dp[i - 1]
    elif s == "OR":
        # OR なら x が True の時は、それまでの y はなんでも良い。
        # x が False の時は、それまでの y は True で無いといけない。
        dp[i] = 2 ** i + dp[i - 1]  # （x = True の時）+（x = False の時）

print(dp[n])
