# -*- coding: utf-8 -*-

n, cp = [int(v) for v in input().split()]

# imos method
status_list = list()
for i in range(n):
    a, b, c = [int(v) for v in input().split()]
    status_list.append((a, c))
    status_list.append((b + 1, -c))

status_list.sort()

ans = 0
cnt_cost = 0
for i in range(len(status_list) - 1):
    data = status_list[i]
    day = data[0]
    cost = data[1]
    cnt_cost += cost

    next_data = status_list[i + 1]
    next_day = next_data[0]
    period = next_day - day

    # プライム料金の方が安いならそちらを利用する。
    if cnt_cost > cp:
        ans += period * cp
    else:
        ans += period * cnt_cost

print(ans)
