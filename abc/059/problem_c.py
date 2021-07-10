import numpy as np
import copy


def check_cum_sum_list(a_list, cum_sum_list, start_id):
    ret_finished_ope = False
    ret_id_should_modify = None
    ret_sign_should_modify = None

    cum_sum = cum_sum_list[start_id]
    for cs_id in range(start_id + 1, len(cum_sum_list)):
        cum_sum += a_list[cs_id]
        cum_sum_list[cs_id] = cum_sum

        if cum_sum_list[cs_id - 1] * cum_sum_list[cs_id] >= 0:
            ret_id_should_modify = cs_id
            ret_sign_should_modify = np.sign(
                cum_sum_list[cs_id - 1]) * -1
            break

    if ret_id_should_modify is None:
        ret_finished_ope = True

    return ret_finished_ope, ret_id_should_modify, ret_sign_should_modify


def get_addition_value(value, sign):
    addition_value = (
        1 + abs(value)) * sign
    return addition_value


def operate_array(a_list, cum_sum_list, id_should_modify, sign_should_modify):
    addition_value = get_addition_value(
        cum_sum_list[id_should_modify], sign_should_modify)
    a_list[id_should_modify] += addition_value
    cum_sum_list[id_should_modify] += addition_value
    ret_count_ope = abs(addition_value)
    return ret_count_ope


def execute(a_list):
    finished_operation = False
    count_ope = 0
    cum_sum_list = [0] * len(a_list)
    cum_sum_list[0] = a_list[0]
    start_id = 0
    while not finished_operation:
        finished_operation, id_should_modify, sign_should_modify = \
            check_cum_sum_list(a_list, cum_sum_list, start_id)

        if id_should_modify is not None:
            count_ope += operate_array(
                a_list, cum_sum_list, id_should_modify, sign_should_modify)
            start_id = id_should_modify
    return count_ope


if __name__ == "__main__":
    n = int(input())
    a_list1 = [int(a) for a in input().split()]
    a_list2 = copy.deepcopy(a_list1)

    count_ope1 = execute(a_list1)

    target_sign2 = np.sign(a_list2[0]) * -1
    addition_value2 = get_addition_value(a_list2[0], target_sign2)
    a_list2[0] += addition_value2
    count_ope2 = abs(addition_value2)
    count_ope2 += execute(a_list2)

    count_ope = min(count_ope1, count_ope2)
    print(count_ope)
