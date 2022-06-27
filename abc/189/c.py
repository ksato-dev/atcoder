

h, w, k = [int(v) for v in input().split()]

mat = [[None] * w for _ in range(h)]

for i in range(h):
    mat[i] = input()

k_cnt = 0
for row_bits in range(2**(h)):
    row_specified_digit = "0" + str(h) + "b"
    row_bits_str = format(row_bits, row_specified_digit)
    for col_bits in range(2**(w)):
        col_specified_digit = "0" + str(w) + "b"
        col_bits_str = format(col_bits, col_specified_digit)

        black_cnt = 0
        for i in range(h):
            row_mask = row_bits_str[i]
            if row_mask == "1":
                continue
            for j in range(w):
                col_mask = col_bits_str[j]
                if col_mask == "1":
                    continue
                if mat[i][j] == "#":
                    black_cnt += 1
        if black_cnt == k:
            k_cnt += 1

print(k_cnt)
