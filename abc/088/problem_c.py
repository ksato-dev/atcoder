import numpy as np


def read_data():
    in_mat = []
    first_line = input()
    first_row_data = first_line.split()
    in_mat.append(first_row_data)
    num_cols = len(first_row_data)

    for _ in range(num_cols - 1):
        curr_line = input()
        curr_row_data = curr_line.split()
        in_mat.append(curr_row_data)

    return (num_cols, in_mat)


def is_in_value_range(value, min, max):
    if min <= value and value <= max:
        return True
    return False


if __name__ == "__main__":
    num_elems, in_mat = read_data()
    in_mat_np_str = np.array(in_mat)
    in_mat_np = in_mat_np_str.astype(np.uint8)

    num_list = range(num_elems)

    max_value = 100
    value_range = range(max_value + 1)

    info_truth = False
    out_a = [-1] * num_elems
    out_b = [-1] * num_elems

    for a0 in value_range:
        invalid = False
        a_valids = [False] * num_elems

        # はじめの行の bj を調べる。
        b_candidates = []
        for col_id in num_list:
            b = in_mat_np[0, col_id] - a0
            invalid = not is_in_value_range(b, 0, max_value)
            b_candidates.append(b)

        # この時点で妥当でなければ飛ばす。
        if invalid:
            continue
        else:
            a_valids[0] = True

        # はじめの行の b0j がわかれば以降の bij もわかる。
        for row_id in range(1, num_elems):
            curr_a_candidates = []
            for col_id in num_list:
                curr_a = in_mat_np[row_id, col_id] - b_candidates[col_id]
                curr_a_candidates.append(curr_a)

            # curr_a_candidates 内の全要素が同じならOK。
            front_a = curr_a_candidates[0]
            valid_curr_a = all(elem == front_a for elem in curr_a_candidates)

            if not valid_curr_a:
                continue

            invalid = not is_in_value_range(front_a, 0, max_value)
            if not invalid:
                a_valids[row_id] = True

        # 最後まで妥当ならOK。
        all_a_valid = all(elem == True for elem in a_valids)
        if all_a_valid:
            info_truth = True
            break

    if info_truth:
        print("Yes")
    else:
        print("No")
