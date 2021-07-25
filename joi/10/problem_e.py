from collections import deque


class CheeseBFS():
    def __init__(self, n, cell_char_mat):
        self.cheese_cost_list = [str(v) for v in range(1, n + 1)]
        self.cell_char_mat = cell_char_mat
        self.num_of_rows = len(self.cell_char_mat)
        self.num_of_cols = len(self.cell_char_mat[0])
        self.cheese_pos_list = [None] * (n+1)
        self.start_rc = None
        self.graph = None

    def check_cell_type(self, r_id, c_id):
        ret_is_in_inner = False
        horizontal_check = 0 <= c_id <= self.num_of_cols - 1
        vertical_check = 0 <= r_id <= self.num_of_rows - 1
        if horizontal_check and vertical_check:
            cell_char = self.cell_char_mat[r_id][c_id]
            is_blank_cell = cell_char == "."
            is_start_cell = cell_char == "S"
            is_cheese_cell = cell_char in self.cheese_cost_list
            if is_blank_cell or is_start_cell or is_cheese_cell:
                ret_is_in_inner = True
        return ret_is_in_inner

    def create_graph(self):
        self.graph = [None] * self.num_of_rows

        for r_id in range(self.num_of_rows):
            self.graph[r_id] = [None] * self.num_of_cols
            for c_id in range(self.num_of_cols):
                cell_char = self.cell_char_mat[r_id][c_id]
                if self.check_cell_type(r_id, c_id):
                    around_ids = [(r_id - 1, c_id), (r_id, c_id - 1),
                                  (r_id + 1, c_id), (r_id, c_id + 1)]
                    adj_list = [
                        rc for rc in around_ids
                        if self.check_cell_type(rc[0], rc[1])]
                    if adj_list:
                        self.graph[r_id][c_id] = adj_list

                    if cell_char == "S":
                        self.start_rc = (r_id, c_id)
                    if cell_char in self.cheese_cost_list:
                        self.cheese_pos_list[int(cell_char)] = (r_id, c_id)

    def calc_dist_to_target_using_bfs(self, start_char, tgt_char):
        start_rc = None
        if start_char == "S":
            start_rc = self.start_rc
        else:
            start_rc = self.cheese_pos_list[int(start_char)]

        tgt_rc = self.cheese_pos_list[int(tgt_char)]

        dist_to_tgt = [
            [None] * self.num_of_cols for _ in range(self.num_of_rows)]

        que = deque()
        que.append(start_rc)
        sr = start_rc[0]
        sc = start_rc[1]
        dist_to_tgt[sr][sc] = 0

        while que:
            nr, nc = que.popleft()

            for adj_rc in self.graph[nr][nc]:
                if adj_rc is None:
                    continue
                ar = adj_rc[0]
                ac = adj_rc[1]
                if dist_to_tgt[ar][ac] is None:
                    dist_to_tgt[ar][ac] = dist_to_tgt[nr][nc] + 1
                    if tgt_rc == adj_rc:
                        return dist_to_tgt[ar][ac]
                    que.append(adj_rc)


if __name__ == "__main__":
    h, w, n = [int(v) for v in input().split()]
    cell_char_matrix = [None] * h
    for row_id in range(h):
        cell_char_matrix[row_id] = [c for c in input()]

    bfs = CheeseBFS(n, cell_char_matrix)
    bfs.create_graph()

    sum_dist = 0
    for cheese_id in bfs.cheese_cost_list:
        if cheese_id == "1":
            sum_dist += bfs.calc_dist_to_target_using_bfs("S", cheese_id)
        else:
            bf_id = str(int(cheese_id) - 1)
            sum_dist += bfs.calc_dist_to_target_using_bfs(bf_id, cheese_id)

    print(sum_dist)
