#!/usr/bin/env python3

from enum import Enum


class Status(Enum):
    UNKNOWN = 0
    MONOTONOUS_INCREASE = 1
    MONOTONOUS_PHENOMENON = 2


def read_a_list():
    line = input()
    arr_str = line.split()
    ret_data = list(map(int, arr_str))

    return ret_data


def read_data():
    line = input()
    ret_data = int(line)

    return ret_data


if __name__ == "__main__":
    N = read_data()
    a_list = read_a_list()

    array_count = 1
    pre_data = a_list[0]
    pre_status = Status.UNKNOWN
    status = Status.UNKNOWN

    for a_id in range(1, len(a_list)):
        data = a_list[a_id]

        is_mono_inc = (data - pre_data > 0)
        is_mono_phen = (data - pre_data < 0)

        if is_mono_inc:
            status = Status.MONOTONOUS_INCREASE
        if is_mono_phen:
            status = Status.MONOTONOUS_PHENOMENON

        is_consecutive = (data == pre_data)
        if is_consecutive:
            pre_data = data
            pre_status = status
            continue

        if pre_status == Status.UNKNOWN:
            pre_status = status

        is_changed_status = status != pre_status
        is_not_unknown = status and pre_status
        if is_changed_status and is_not_unknown:
            array_count += 1
            pre_status = Status.UNKNOWN
        else:
            pre_status = status

        pre_data = data

    print(array_count)
