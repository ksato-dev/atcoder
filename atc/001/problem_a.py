# ref: https://qiita.com/enbi/items/245c974fb6e62a8e238c
import sys  # 追加
sys.setrecursionlimit(500*500)  # 追加


def check_char(cell_char):
    ret_valid = False
    if cell_char == "." or cell_char == "s" or cell_char == "g":
        ret_valid = True
    return ret_valid


def get_adjacency_list(cell_matrix, row_id, col_id):
    h = len(cell_matrix)
    w = len(cell_matrix[0])
    center = cell_matrix[row_id][col_id]
    ret_adj_list = None
    if check_char(center):
        ret_adj_list = []
        if 0 < row_id:
            top = cell_matrix[row_id - 1][col_id]
            if check_char(top):
                ret_adj_list.append([row_id - 1, col_id])
        if row_id < h - 1:
            bottom = cell_matrix[row_id + 1][col_id]
            if check_char(bottom):
                ret_adj_list.append([row_id + 1, col_id])
        if 0 < col_id:
            left = cell_matrix[row_id][col_id - 1]
            if check_char(left):
                ret_adj_list.append([row_id, col_id - 1])
        if col_id < w - 1:
            right = cell_matrix[row_id][col_id + 1]
            if check_char(right):
                ret_adj_list.append([row_id, col_id + 1])

    return ret_adj_list


def dfs(cell_matrix, graph, seen, row_id, col_id):
    w = len(cell_matrix[0])
    seen[row_id][col_id] = True

    if cell_matrix[row_id][col_id] == "g":
        return True

    for adj_rc in graph[row_id * w + col_id]:
        adj_col_id = adj_rc % w
        adj_row_id = int(adj_rc / w)

        if seen[adj_row_id][adj_col_id]:
            continue
        if dfs(cell_matrix, graph, seen, adj_row_id, adj_col_id):
            return True

    return False


if __name__ == "__main__":
    h, w = [int(v) for v in input().split()]

    seen = [[False] * w for _ in range(h)]
    graph = [None] * w * h

    cell_matrix = [None] * h

    start_row = None
    start_col = None
    for row_id in range(h):
        line_str = input()
        cell_chars = [c for c in line_str]
        cell_matrix[row_id] = cell_chars
        temp_start_col = line_str.find("s")
        if temp_start_col >= 0:
            start_col = temp_start_col
            start_row = row_id

    for row_id in range(h):
        for col_id in range(w):
            curr_adj_list = get_adjacency_list(cell_matrix, row_id, col_id)
            if curr_adj_list is not None:
                g_id = row_id * w + col_id
                graph[g_id] = []
                for adj_rc in curr_adj_list:
                    graph[g_id].append(adj_rc[0] * w + adj_rc[1])

    if dfs(cell_matrix, graph, seen, start_row, start_col):
        print("Yes")
    else:
        print("No")
