# -*- coding: utf-8 -*-
import copy

if __name__ == "__main__":
    n, q = [int(v) for v in input().split()]
    num_list = [i for i in range(0, n+1)]
    swap_list = [i for i in range(0, n+1)]
    for i in range(q):
        x = int(input())
        # swap_id = num_list.index(x)
        # print(x, swap_list)
        swap_id = swap_list[x]

        if swap_id < n:
            tmp_num = copy.deepcopy(num_list[swap_id])
            swap_num = copy.deepcopy(num_list[swap_id+1])
            num_list[swap_id] = swap_num
            num_list[swap_id+1] = tmp_num

            swap_list[swap_num] = swap_id
            swap_list[tmp_num] = swap_id+1
        elif swap_id == n:
            tmp_num = copy.deepcopy(num_list[swap_id])
            swap_num = copy.deepcopy(num_list[swap_id-1])
            num_list[swap_id] = swap_num
            num_list[swap_id-1] = tmp_num

            swap_list[swap_num] = swap_id
            swap_list[tmp_num] = swap_id-1

    print(" ".join(map(str, num_list[1:])))
