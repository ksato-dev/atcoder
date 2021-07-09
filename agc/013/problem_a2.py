#!/usr/bin/env python3

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
    pre_status = None
    skip_flag = False

    for a_id in range(1, len(a_list)):
        data = a_list[a_id]

        is_mono_inc = (data - pre_data > 0)
        is_mono_phen = (data - pre_data < 0)

        if is_mono_inc:
            status = 1
        elif is_mono_phen:
            status = -1
        else:
            continue

        if pre_status is None:
            pre_status = status

        is_changed_status = status != pre_status
        if is_changed_status and not skip_flag:
            array_count += 1
            skip_flag = True
        else:
            skip_flag = False

        pre_status = status
        pre_data = data

    print(array_count)
