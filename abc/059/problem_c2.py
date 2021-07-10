import numpy as np
import copy


def simulation(a_list):
    sum_a = 0
    count_ope = 0
    for arr_id, a in enumerate(a_list):
        current_sum_a = sum_a + a
        if arr_id == 0:
            sum_a = current_sum_a
            continue

        if sum_a * current_sum_a < 0:
            sum_a = current_sum_a
        else:
            flip_sign = None
            if np.sign(current_sum_a) < 0:
                flip_sign = 1
            elif np.sign(current_sum_a) > 0:
                flip_sign = -1

            count_ope += abs(current_sum_a) + 1
            current_sum_a = flip_sign
            sum_a = current_sum_a

    return count_ope


if __name__ == "__main__":
    n = int(input())
    a_list1 = [int(a) for a in input().split()]
    a_list2 = copy.deepcopy(a_list1)

    count_ope1 = 0
    count_ope2 = 0
    if a_list1[0] == 0:
        a_list1[0] = 1
        count_ope1 = 1
        a_list2[0] = -1
        count_ope2 = 1
    else:
        flip_sign = np.sign(a_list2[0]) * -1
        count_ope2 = abs(a_list2[0]) + 1
        a_list2[0] = flip_sign

    count_ope1 += simulation(a_list1)
    count_ope2 += simulation(a_list2)

    count_ope = min(count_ope1, count_ope2)
    print(count_ope)
