import numpy as np
from numba import njit


# @njit
def main():
    n = int(input())

    min_r, min_c = 1e10, 1e10
    max_r, max_c = -1, -1

    r_list = []
    c_list = []
    r_append = r_list.append
    c_append = c_list.append
    for _ in range(n):
        c, r = [int(v) for v in input().split()]
        if c < min_c:
            min_c = c
        if max_c < c:
            max_c = c
        if r < min_r:
            min_r = r
        if max_r < r:
            max_r = r
        r_append(r)
        c_append(c)

    # 必要ない範囲（0のみの所）は除外する
    width = max_c - min_c + 1
    height = max_r - min_r + 1
    grid_data = np.zeros((height, width))
    for list_id in range(n):
        r = r_list[list_id]
        c = c_list[list_id]

        grid_data[r - min_r, c - min_c] = 1

    print(grid_data)

    for r in range(height):
        check_row = np.sum(grid_data[r])
        if check_row < 2:
            grid_data[r] = 0

    print(grid_data)

    for c in range(width):
        check_col = np.sum(grid_data[:, c])
        if check_col < 2:
            grid_data[:, c] = 0

    print(grid_data)

    # 座標圧縮して余白を消したほうが良さそう。

    # exit()

    row_width_list = [None] * height
    for r in range(height):
        check_row = 0
        min_c = height * 2
        max_c = -1
        for c in range(width):
            if grid_data[r, c] == 1:
                check_row = check_row + 1
                if c < min_c:
                    min_c = c
                if max_c < c:
                    max_c = c

        if check_row >= 2:
            row_width_list[r] = (min_c, max_c)

    print(row_width_list)

    pre_row_width = None
    split_id_list = []
    for r_id, row_width in enumerate(row_width_list):
        if pre_row_width != row_width:
            split_id_list.append(r_id)
        pre_row_width = row_width

    print(split_id_list)


if __name__ == "__main__":
    main()
