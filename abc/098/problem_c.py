def is_east(c):
    ret_flag = True
    if c == "W":
        ret_flag = False
    return ret_flag


if __name__ == "__main__":
    n = int(input())
    s = input()

    # calculate cumulative sum list.
    total_people_num = len(s)
    cum_sum_e_list = [0] * (total_people_num + 1)
    cum_sum_w_list = [0] * (total_people_num + 1)
    for c_id, c in enumerate(s):
        if is_east(c):
            cum_sum_e_list[c_id + 1] = cum_sum_e_list[c_id] + 1
            cum_sum_w_list[c_id + 1] = cum_sum_w_list[c_id]
        else:
            cum_sum_w_list[c_id + 1] = cum_sum_w_list[c_id] + 1
            cum_sum_e_list[c_id + 1] = cum_sum_e_list[c_id]

    # judge
    min_num_of_need_to_change = 10**18
    for c_id, c in enumerate(s):
        num_of_need_to_change_in_east_side = 0
        if c_id < total_people_num - 1:
            num_in_east_side = total_people_num - (c_id + 1)
            west_num_in_east_side = cum_sum_w_list[total_people_num
                                                   ] - cum_sum_w_list[c_id + 1]
            num_of_need_to_change_in_east_side = num_in_east_side \
                - west_num_in_east_side

        num_of_need_to_change_in_west_side = 0
        if 0 < c_id:
            num_in_west_side = c_id
            east_num_in_west_side = cum_sum_e_list[c_id] - cum_sum_e_list[0]
            num_of_need_to_change_in_west_side = num_in_west_side \
                - east_num_in_west_side

        cand_min_num = num_of_need_to_change_in_east_side + \
            num_of_need_to_change_in_west_side
        min_num_of_need_to_change = \
            min(min_num_of_need_to_change, cand_min_num)

    print(min_num_of_need_to_change)
