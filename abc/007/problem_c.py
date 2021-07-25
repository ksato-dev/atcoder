from queue import Queue


def bfs(graph, cell_char_mat, dist, sx, sy, gx, gy):
    dist[sx][sy] = 0
    que = Queue()
    que.put((sx, sy))
    while not que.empty():
        next_cell = que.get()
        nx = next_cell[0]
        ny = next_cell[1]
        for adj_cell in graph[nx][ny]:
            ax = adj_cell[0]
            ay = adj_cell[1]
            if dist[ax][ay] is None:
                dist[ax][ay] = dist[nx][ny] + 1
                que.put((ax, ay))


def check_cell_type(cell_char_mat, r_id, c_id, r, c):
    ret_is_in_inner = False
    horizontal_check = 0 <= c_id <= c-1
    vertical_check = 0 <= r_id <= r-1
    if horizontal_check and vertical_check:
        if cell_char_matrix[r_id][c_id] == ".":
            ret_is_in_inner = True
    return ret_is_in_inner


def create_graph(graph, cell_char_mat, r, c):

    for r_id in range(r):
        for c_id in range(c):
            curr_cell = cell_char_matrix[r_id][c_id]
            if curr_cell == ".":
                adj_list = []
                if check_cell_type(cell_char_matrix, r_id - 1, c_id, r, c):
                    adj_list.append((r_id - 1, c_id))
                if check_cell_type(cell_char_matrix, r_id, c_id - 1, r, c):
                    adj_list.append((r_id, c_id - 1))
                if check_cell_type(cell_char_matrix, r_id + 1, c_id, r, c):
                    adj_list.append((r_id + 1, c_id))
                if check_cell_type(cell_char_matrix, r_id, c_id + 1, r, c):
                    adj_list.append((r_id, c_id + 1))
                if adj_list:
                    graph[r_id][c_id] = adj_list


if __name__ == "__main__":
    r, c = [int(v) for v in input().split()]
    sx, sy = [int(v) - 1 for v in input().split()]
    gx, gy = [int(v) - 1 for v in input().split()]
    cell_char_matrix = [None] * r
    dist = [None] * r
    graph = [None] * r
    for row_id in range(r):
        cell_char_matrix[row_id] = [c for c in input()]
        dist[row_id] = [None] * c
        graph[row_id] = [None] * c

    create_graph(graph, cell_char_matrix, r, c)
    bfs(graph, cell_char_matrix, dist, sx, sy, gx, gy)
    print(dist[gx][gy])
