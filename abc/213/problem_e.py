import sys
sys.setrecursionlimit(1000000)

def dfs(graph, cell_char_matrix, nx, ny, gx, gy, min_cnt):
    for adj_xy in graph[nx][ny]:
        temp_min_cnt = 10**8
        dfs(graph, adj_xy[0], adj_xy[1], gx, gy, temp_min_cnt)
        if (nx, ny) == (0, 0):
            min_cnt = min(min_cnt, temp_min_cnt)


def check_cell_pos(r_id, c_id, r, c):
    ret_is_in_inner = False
    horizontal_check = 0 <= c_id <= c-1
    vertical_check = 0 <= r_id <= r-1
    if horizontal_check and vertical_check:
        ret_is_in_inner = True
    return ret_is_in_inner


def create_graph(graph, cell_char_mat, r, c):

    for r_id in range(r):
        for c_id in range(c):
            adj_list = []
            if check_cell_pos(r_id - 1, c_id, r, c):
                adj_list.append((r_id - 1, c_id))
            if check_cell_pos(r_id, c_id - 1, r, c):
                adj_list.append((r_id, c_id - 1))
            if check_cell_pos(r_id + 1, c_id, r, c):
                adj_list.append((r_id + 1, c_id))
            if check_cell_pos(r_id, c_id + 1, r, c):
                adj_list.append((r_id, c_id + 1))
            if adj_list:
                graph[r_id][c_id] = adj_list


if __name__ == "__main__":
    r, c = [int(v) for v in input().split()]
    sx, sy = 0, 0
    gx, gy = r-1, c-1
    cell_char_matrix = [None] * r
    dist = [None] * r
    graph = [None] * r
    for row_id in range(r):
        cell_char_matrix[row_id] = [c for c in input()]
        dist[row_id] = [None] * c
        graph[row_id] = [None] * c

    create_graph(graph, cell_char_matrix, r, c)
    min_cnt = 10 ** 8
    dfs(graph, cell_char_matrix, sx, sy, gx, gy, min_cnt)
    if min_cnt == 10 ** 8:
        print(0)
    else:
        print(min_cnt)
