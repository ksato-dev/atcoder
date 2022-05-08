# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, a, b = [int(v) for v in input().split()]

    h = a * n
    w = b * n
    white_tile = False
    for r_cnt in range(h):
        ans_str = ""
        if (r_cnt // a) % 2 == 0:
            white_tile = True
        else:
            white_tile = False
        for c_cnt in range(w):
            if c_cnt % b == 0 and c_cnt > 0:
                white_tile = not white_tile
            if white_tile:
                ans_str += "."
            else:
                ans_str += "#"
        print(ans_str)
