import numpy as np


def calc_cumulative_sum(array_data):
    if not array_data:
        return None

    ret_array = [array_data[0]]
    cum_sum = array_data[0]
    for a_id in range(1, len(array_data)):
        cum_sum += array_data[a_id]
        ret_array.append(cum_sum)

    return ret_array


def check_cum_sum_list(cum_sum_list):
    ret_finished_ope = False
    ret_id_should_modify = None
    ret_sign_should_modify = None

    for cs_id in range(1, len(cum_sum_list)):
        if cum_sum_list[cs_id - 1] * cum_sum_list[cs_id] >= 0:
            ret_id_should_modify = cs_id
            ret_sign_should_modify = np.sign(
                cum_sum_list[cs_id - 1]) * -1
            break

    if ret_id_should_modify is None:
        ret_finished_ope = True

    return ret_finished_ope, ret_id_should_modify, ret_sign_should_modify


def operate_array(a_list, cum_sum_list, id_should_modify, sign_should_modify):
    addition_value = (
        1 + abs(cum_sum_list[id_should_modify])) * sign_should_modify
    a_list[id_should_modify] += addition_value
    ret_count_ope = abs(addition_value)
    return ret_count_ope


if __name__ == "__main__":
    n = int(input())
    a_list = [int(a) for a in input().split()]

    finished_operation = False
    count_ope = 0
    while not finished_operation:
        cum_sum_list = calc_cumulative_sum(a_list)
        finished_operation, id_should_modify, sign_should_modify = \
            check_cum_sum_list(cum_sum_list)

        if id_should_modify is not None:
            count_ope += operate_array(
                a_list, cum_sum_list, id_should_modify, sign_should_modify)

    print(count_ope)
