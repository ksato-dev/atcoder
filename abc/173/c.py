
h, w, k = [int(v) for v in input().split()]

c_map = [[None] * w for _ in range(h)]
for i in range(h):
    raw_str = input()
    for j, c in enumerate(raw_str):
        int_c = (c == "#") if 1 else 0
        c_map[i][j] = int_c

# print(c_map)
sum_all_black = sum([sum(c_row) for c_row in c_map])

comb_cnt = 0
for row_bits_dec in range(2**h):
    specified_digit = "0" + str(h) + "b"
    row_bits_str = format(row_bits_dec, specified_digit)

    for col_bits_dec in range(2**w):
        specified_digit = "0" + str(w) + "b"
        col_bits_str = format(col_bits_dec, specified_digit)
        # sum_col = sum([int(c) for c in col_bits_str])

        curr_sum_black = 0
        for i in range(h):
            # 塗る行は飛ばす
            if row_bits_str[i] == "1":
                continue

            for j in range(w):
                # 塗る列は飛ばす
                if col_bits_str[j] == "1":
                    continue

                if c_map[i][j]:
                    curr_sum_black += 1

        if k == curr_sum_black:
            comb_cnt += 1

print(comb_cnt)
