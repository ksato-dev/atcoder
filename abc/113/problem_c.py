def bin_search(sorted_list, desired_val):
    front_id = 0
    end_id = len(sorted_list) - 1

    ret_found_val = False
    ret_tgt_id = -1
    while end_id >= front_id:
        tgt_id = front_id + int((end_id - front_id) / 2)
        val = sorted_list[tgt_id]
        if desired_val == val:
            ret_found_val = True
            ret_tgt_id = tgt_id
            break
        elif val < desired_val:
            front_id = tgt_id + 1
        elif desired_val < val:
            end_id = tgt_id - 1

    return ret_found_val, ret_tgt_id


def get_zero_padding(num_digits, dec_num):
    bin_digits = "0" + str(num_digits) + "d"
    ans_str = format(dec_num, bin_digits)
    return ans_str


if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    p_list = []
    y_list = []

    p_y_table = {n_id: list() for n_id in range(n + 1)}
    for i in range(m):
        p_i, y_i = [int(v) for v in input().split()]
        p_list.append(p_i)
        y_list.append(y_i)
        p_y_table[p_i].append(y_i)

    for p_i in range(n):
        acutual_p_i = p_i + 1
        p_y_table[acutual_p_i].sort()

    for i in range(m):
        p_id = p_list[i]
        y_i = y_list[i]
        birth_year_list = p_y_table[p_id]
        found, city_id = bin_search(birth_year_list, y_i)
        actual_city_id = city_id + 1
        ans_str = get_zero_padding(
            6, p_id) + get_zero_padding(6, actual_city_id)
        print(ans_str)
