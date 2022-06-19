# -*- coding: utf-8 -*-

n = int(input())
a_list = [int(v) for v in input().split()]

p = 0

agent_list = list()
for i in range(n):
    agent_list.append(0)
    a = a_list[i]
    
    delete_list = []
    for a_id, _ in enumerate(agent_list):
        agent_list[a_id] += a
        if agent_list[a_id] >= 4:
            delete_list.append(a_id)
            p += 1

    for d_id in reversed(delete_list):
        agent_list.pop(d_id)

print(p)
