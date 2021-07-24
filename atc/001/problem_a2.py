def check_char(cell_char):
    ret_valid = False
    if cell_char == "." or cell_char == "s" or cell_char == "g":
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


def dfs(seen, cell_matrix, s_cell_id, w, h):
    todo = list()
    cell_id = s_cell_id
    while True:
        seen[cell_id] = True

        if cell_matrix[cell_id] == "g":
            return True

        adj_list = get_adjacency_list(cell_matrix, cell_id, w, h)
        if adj_list:
            todo.extend(adj_list)

        while todo:
            next_id = todo.pop()
            if seen[next_id]:
                continue
            cell_id = next_id
            break

        if seen[cell_id]:
            break

    return False


if __name__ == "__main__":
    h, w = [int(v) for v in input().split()]

    seen = [False] * w * h
    graph = [None] * w * h

    cell_matrix = []  # attention: This array is 1-dim.

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

    for row_id in range(h):
        for col_id in range(w):
            cell_id = ij_to_id(row_id, col_id, w)
            curr_adj_list = get_adjacency_list(cell_matrix, cell_id, w, h)
            if curr_adj_list is not None:
                graph[cell_id] = []
                for adj_rc in curr_adj_list:
                    graph[cell_id].append(adj_rc)

    start_cell_id = ij_to_id(start_row, start_col, w)
    if dfs(seen, cell_matrix, start_cell_id, w, h):
        print("Yes")
    else:
        print("No")
