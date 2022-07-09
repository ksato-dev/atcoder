# -*- coding: utf-8 -*-

n = int(input())

x_list = [0] * n  # x = (takahashi voting num) - (aoki voting num)
x_sum = 0

for i in range(n):
    a, b = [int(v) for v in input().split()]
    x_list[i] = (a + b) - (-a)
    x_sum -= a

# 高橋氏がどこでも演説しない場合、x_sum = sum(a_list) * -1

# x が大きい順に調べる。
cnt = 0
x_list.sort(reverse=True)
for x in x_list:
    x_sum += x
    cnt += 1
    if x_sum > 0:
        break

print(cnt)
