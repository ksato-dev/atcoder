# -*- coding: utf-8 -*-


n = int(input())
s = input()
merged_pc_list = [(int(v), -int(s[i])) for i, v in enumerate(input().split())]

# -1 倍してソートすることで、体重が同じ大人と子供がいても、右側に大人が寄る。
merged_pc_list.sort()

s_m_t_list = [0] * (n + 1)
for i in range(n):
    s_m_t_list[i+1] = -merged_pc_list[i][1] + s_m_t_list[i]

max_num = -1
# num_person = n - s.count("0")
for i in range(n + 1):
    sum_person_right = s_m_t_list[n] - s_m_t_list[i]
    sum_person_left = s_m_t_list[i] - s_m_t_list[0]
    sum_child = i - sum_person_left
    max_num = max(max_num, sum_child + sum_person_right)

print(max_num)
