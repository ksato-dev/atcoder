# -*- coding: utf-8 -*-

n = int(input())

# imos method
login_list = list()
for i in range(n):
    a, b = [int(v) for v in input().split()]
    login_list.append((a, 1))  # login
    login_list.append((a + b, -1))  # logout

login_list.sort()  # first key で sort（ログイン順にソート）

login_period_table = [0] * (n + 1)
cnt_people = 0
for t in range(len(login_list) - 1):
    data = login_list[t]
    cnt_people += data[1]
    next_data = login_list[t + 1]
    login_period_table[cnt_people] += (next_data[0] - data[0])

for i in range(n):
    print(login_period_table[i+1], end=" ")
print()
