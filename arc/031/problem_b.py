def check_char(cell_char):
    ret_valid = False
    if cell_char == "o":
        ret_valid = True
    return ret_valid


def check_out_of_boundary(row_id, col_id, w, h):
    ret_is_inner = False
    not_over_top = 0 <= row_id
    not_over_btm = row_id <= h - 1
    not_over_lft = 0 <= col_id
    not_over_rgt = col_id <= w - 1

    if not_over_top and not_over_btm and not_over_lft and not_over_rgt:
        ret_is_inner = True

    return ret_is_inner


def get_adjacency_list(cell_matrix, cell_id, w, h):
    row_id = int(cell_id / w)
    col_id = cell_id % w
    tgt_cell = cell_matrix[cell_id]
    ret_adj_list = None
    if check_char(tgt_cell):
        ret_adj_list = []

        candidate_ids = []
        if check_out_of_boundary(row_id - 1, col_id, w, h):
            candidate_ids.append(ij_to_id(row_id - 1, col_id, w))
        if check_out_of_boundary(row_id + 1, col_id, w, h):
            candidate_ids.append(ij_to_id(row_id + 1, col_id, w))
        if check_out_of_boundary(row_id, col_id - 1, w, h):
            candidate_ids.append(ij_to_id(row_id, col_id - 1, w))
        if check_out_of_boundary(row_id, col_id + 1, w, h):
            candidate_ids.append(ij_to_id(row_id, col_id + 1, w))

        for cand_id in candidate_ids:
            if check_char(cell_matrix[cand_id]):
                ret_adj_list.append(cand_id)

    return ret_adj_list


def ij_to_id(row_id, col_id, width):
    g_id = int(row_id * width + col_id)
    return g_id


def check_area_ids_on_around_cell(area_id_matrix, cell_id,
                                  all_area_id_list, w, h):
    row_id = int(cell_id / w)
    col_id = cell_id % w

    cell_ids_on_arround = []
    if check_out_of_boundary(row_id - 1, col_id, w, h):
        cell_ids_on_arround.append(ij_to_id(row_id - 1, col_id, w))
    if check_out_of_boundary(row_id + 1, col_id, w, h):
        cell_ids_on_arround.append(ij_to_id(row_id + 1, col_id, w))
    if check_out_of_boundary(row_id, col_id - 1, w, h):
        cell_ids_on_arround.append(ij_to_id(row_id, col_id - 1, w))
    if check_out_of_boundary(row_id, col_id + 1, w, h):
        cell_ids_on_arround.append(ij_to_id(row_id, col_id + 1, w))

    area_ids_on_arround = [area_id_matrix[c_id]
                           for c_id in cell_ids_on_arround]
    if not area_ids_on_arround:
        return False

    ret_flag = True
    for area_id in all_area_id_list:
        if area_id not in area_ids_on_arround:
            ret_flag = False

    return ret_flag


def fill_cells_using_dfs(area_id_matrix, area_id,
                         cell_matrix, s_cell_id, w, h):
    todo = list()
    cell_id = s_cell_id
    while True:
        area_id_matrix[cell_id] = area_id

        adj_list = get_adjacency_list(cell_matrix, cell_id, w, h)
        if adj_list:
            todo.extend(adj_list)

        while todo:
            next_id = todo.pop()
            if area_id_matrix[next_id] >= 0:
                continue
            cell_id = next_id
            break

        if area_id_matrix[cell_id] >= 0:
            break


if __name__ == "__main__":
    h, w = 10, 10

    area_id_matrix = [-1] * w * h
    graph = [None] * w * h

    cell_matrix = []  # attention: This array is 1-dim.

    # get input data ---
    start_row = None
    start_col = None
    for row_id in range(h):
        line_str = input()
        cell_chars = [c for c in line_str]
        cell_matrix.extend(cell_chars)
        temp_start_col = line_str.find("s")
        if temp_start_col >= 0:
            start_col = temp_start_col
            start_row = row_id
    # --- get input data

    # create graph ---
    for row_id in range(h):
        for col_id in range(w):
            cell_id = ij_to_id(row_id, col_id, w)
            curr_adj_list = get_adjacency_list(cell_matrix, cell_id, w, h)
            if curr_adj_list is not None:
                graph[cell_id] = []
                for adj_rc in curr_adj_list:
                    graph[cell_id].append(adj_rc)
    # --- create graph

    area_id = 0
    all_area_id_list = list()
    for cell_id, cell_char in enumerate(cell_matrix):
        gave_area_id = area_id_matrix[cell_id] != -1
        if check_char(cell_char) and not gave_area_id:
            fill_cells_using_dfs(area_id_matrix, area_id,
                                 cell_matrix, cell_id, w, h)
            all_area_id_list.append(area_id)
            area_id = area_id + 1

    for cell_id, cell_char in enumerate(cell_matrix):
        if not check_char(cell_char):
            all_area_ids_is_in_arround_cells = check_area_ids_on_around_cell(
                area_id_matrix, cell_id, all_area_id_list, w, h)
            if all_area_ids_is_in_arround_cells:
                print("YES")
                exit()

    print("NO")
