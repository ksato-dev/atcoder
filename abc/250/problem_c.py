# -*- coding: utf-8 -*-
# import copy
import numpy as np
from numba import njit

@njit
def solve(n, q, np_num_list, np_x_list):
    for x in np_x_list:
        # swap_id = np_num_list.index(x)
        swap_id = np.where(np_num_list == x)[0][0]
        length = len(np_num_list) - 1

        if swap_id < length:
            # tmp_num = copy.deepcopy(np_num_list[swap_id])
            # swap_num = copy.deepcopy(np_num_list[swap_id+1])
            tmp_num = np_num_list[swap_id]
            swap_num = np_num_list[swap_id+1]
            np_num_list[swap_id] = swap_num
            np_num_list[swap_id+1] = tmp_num
        elif swap_id == length:
            # tmp_num = copy.deepcopy(np_num_list[swap_id])
            # swap_num = copy.deepcopy(np_num_list[swap_id-1]) #
            tmp_num = np_num_list[swap_id]
            swap_num = np_num_list[swap_id-1]
            np_num_list[swap_id] = swap_num
            np_num_list[swap_id-1] = tmp_num
    return np_num_list


if __name__ == "__main__":
    n, q = [int(v) for v in input().split()]
    np_num_list = np.array([i for i in range(1, n+1)])
    x_list = list()
    for i in range(q):
        x_list.append(int(input()))
    np_x_list = np.array(x_list)
    ans_list = solve(n, q, np_num_list, np_x_list)
    ans_list = [str(ans) for ans in ans_list]
    print(" ".join(ans_list))
