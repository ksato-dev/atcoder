def check_cell_type(cell_char_mat, r_id, c_id, row_num, col_num):
    ret_is_in_inner = False
    horizontal_check = 0 <= c_id <= col_num-1
    vertical_check = 0 <= r_id <= row_num-1
    if horizontal_check and vertical_check:
        if cell_char_mat[r_id][c_id] == "#":
            ret_is_in_inner = True
    return ret_is_in_inner


def count_around_cells(cell_char_mat, r_id, c_id, row_num, col_num):
    ret_count = 0
    cell_ids = [(r_id - 1, c_id - 1), (r_id, c_id - 1), (r_id + 1, c_id - 1),
                (r_id + 1, c_id), (r_id + 1, c_id + 1), (r_id, c_id + 1),
                (r_id - 1, c_id + 1), (r_id - 1, c_id)]
    for cell in cell_ids:
        if check_cell_type(cell_char_mat, cell[0], cell[1], row_num, col_num):
            ret_count = ret_count + 1

    return ret_count


if __name__ == "__main__":
    h, w = [int(v) for v in input().split()]
    cell_data = [None] * h
    for h_id in range(h):
        cell_data[h_id] = input()

    for h_id in range(h):
        row_str = ""
        for w_id in range(w):
            count = 0
            curr_cell_is_bomb = check_cell_type(cell_data, h_id, w_id, h, w)
            if not curr_cell_is_bomb:
                count = count_around_cells(cell_data, h_id, w_id, h, w)
                row_str = row_str + str(count)
            else:
                row_str = row_str + "#"

        print(row_str)
