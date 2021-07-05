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

    info_truth = False

    division_count = 0
    just_done = False
    peak_cnt = 0

    for a_id in range(1, len(a_list) - 1):
        if not just_done:
            diff_minus = a_list[a_id] - a_list[a_id - 1]
            diff_plus = a_list[a_id + 1] - a_list[a_id]
            if diff_minus * diff_plus < 0:
                peak_cnt += 1
                just_done = True
        else:
            # after found peak, skip once.
            just_done = False

    print(peak_cnt + 1)
