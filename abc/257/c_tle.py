# -*- coding: utf-8 -*-

n = int(input())
s = input()
w_list = [int(v) for v in input().split()]

person_list = []
child_list = []
p_append = person_list.append
c_append = child_list.append

for i, c in enumerate(s):
    w = w_list[i]
    if c == "0":
        c_append((w, 0))
    elif c == "1":
        p_append((w, 1))

merged_pc_list = child_list + person_list

# print(merged_pc_list)
merged_pc_list.sort()
# print(merged_pc_list)

m_w_list = [data[0] for data in merged_pc_list]
m_t_list = [data[1] for data in merged_pc_list]

max_num = -1
for i in range(len(merged_pc_list)):
    weight = m_w_list[i]
    type = m_t_list[i]

    sum_person = sum(m_t_list[i:])
    sum_child = len(m_t_list[:i]) - sum(m_t_list[:i])
    if i < len(merged_pc_list) - 1:
        next_weight = m_w_list[i+1]
        # ２以上ずれてるなら１個ずらせる
        if next_weight - weight >= 2:
            sum_person = sum(m_t_list[i+1:])
            sum_child = len(m_t_list[:i+1]) - sum(m_t_list[:i+1])
    elif i == len(merged_pc_list) - 1 and type == 0:
        sum_child = len(m_t_list[:i+1]) - sum(m_t_list[:i+1])

    # print("sum_child:", sum_child, "sum_person:", sum_person)
    if max_num < sum_child + sum_person:
        max_num = sum_child + sum_person

print(max_num)
