import numpy as np
# from numba import njit


# @njit
def extract_valid_area_by_use_bbox(src_list):
    min_r = 500
    min_c = 500
    max_r = -1
    max_c = -1

    n = len(src_list)
    for row_id in range(n):
        for col_id in range(n):
            if src_list[row_id, col_id] == "#":
                if row_id < min_r:
                    min_r = row_id
                if col_id < min_c:
                    min_c = col_id
                if max_r < row_id:
                    max_r = row_id
                if max_c < col_id:
                    max_c = col_id

    desired_list = src_list[min_r:max_r+1, min_c:max_c+1]
    return desired_list


if __name__ == "__main__":
    n = int(input())
    s_list = [None] * n
    for s_id in range(n):
        s_list[s_id] = list(input())

    t_list = [None] * n
    for t_id in range(n):
        t_list[t_id] = list(input())

    s_list = np.array(s_list, dtype=str)
    t_list = np.array(t_list, dtype=str)

    extracted_s_list = extract_valid_area_by_use_bbox(s_list)
    extracted_t_list = extract_valid_area_by_use_bbox(t_list)
   
    match_flag = np.array_equal(extracted_s_list, extracted_t_list)

    # ref: https://www.fixes.pub/program/441198.html
    if not match_flag:
        for _ in range(3):
            extracted_s_list = np.rot90(extracted_s_list, k=1, axes=(1, 0))
            match_flag = np.array_equal(extracted_s_list, extracted_t_list)
            if match_flag:
                break

    if match_flag:
        print("Yes")
    else:
        print("No")
