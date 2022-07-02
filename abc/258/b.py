# -*- coding: utf-8 -*-

n = int(input())
mat = [0] * n

for i in range(n):
    col = input()
    mat[i] = [int(v) for v in col]
    for j in range(n):
        curr_val = mat[i][j]

# max_id を中心に８方向見る。
dir_list = [[1, 0], [1, 1], [0, 1], [-1, 1],
            [-1, 0], [-1, -1], [0, -1], [1, -1]]
# max_id = tuple(max_id)
max_seq_val = 0
for i in range(n):
    for j in range(n):
        for curr_dir in dir_list:
            curr_seq_str = str(mat[i][j])
            curr_id = [i, j]
            for step in range(n-1):
                curr_id[0] += curr_dir[0]
                curr_id[1] += curr_dir[1]

                if curr_id[0] < 0:
                    curr_id[0] = n - 1
                elif n <= curr_id[0]:
                    curr_id[0] = 0
                if curr_id[1] < 0:
                    curr_id[1] = n - 1
                elif n <= curr_id[1]:
                    curr_id[1] = 0

                curr_val = mat[curr_id[0]][curr_id[1]]
                curr_seq_str += str(curr_val)

            curr_seq_val = int(curr_seq_str)
            if max_seq_val < curr_seq_val:
                max_seq_val = curr_seq_val

print(max_seq_val)
