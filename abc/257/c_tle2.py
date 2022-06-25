# -*- coding: utf-8 -*-

import numpy as np
from numba import njit


@njit
def main(merged_pc_list):
    merged_pc_list = np.array(merged_pc_list)

    # m_w_list = [data[0] for data in merged_pc_list]
    # m_t_list = [data[1] for data in merged_pc_list]
    m_w_list = merged_pc_list[:, 0]
    m_t_list = merged_pc_list[:, 1]

    max_num = -1
    num_m_pc_list = merged_pc_list.shape[0]

    for i in range(num_m_pc_list):
        weight = m_w_list[i]
        type = m_t_list[i]

        sub_m_t_list1 = m_t_list[i:]
        sum_person = np.sum(sub_m_t_list1)
        # sub_m_t_list2 = m_t_list[:i]
        sum_sub_m_t_list2 = np.sum(m_t_list[:i])
        sum_child = m_t_list[:i].shape[0] - sum_sub_m_t_list2
        if i < num_m_pc_list - 1:
            next_weight = m_w_list[i+1]
            # next_type = m_t_list[i+1]
            # ２以上ずれてるなら１個ずらせる
            if next_weight - weight >= 2:
                sum_person = np.sum(m_t_list[i+1:])
                sum_child = m_t_list[:i+1].shape[0] - np.sum(m_t_list[:i+1])
                # sum_child = m_t_list[:i+1].shape[0] - (sum_sub_m_t_list2 + (1 - next_type))
        elif i == num_m_pc_list - 1 and type == 0:
            sum_child = m_t_list[:i+1].shape[0] - np.sum(m_t_list[:i+1])
            # sum_child = m_t_list[:i+1].shape[0] - (sum_sub_m_t_list2 + (1 - next_type))

        # print("sum_child:", sum_child, "sum_person:", sum_person)
        if max_num < sum_child + sum_person:
            max_num = sum_child + sum_person

    print(max_num)


if __name__ == "__main__":
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
    merged_pc_list.sort()

    main(merged_pc_list)
