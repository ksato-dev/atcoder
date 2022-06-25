# -*- coding: utf-8 -*-


n, k, q = [int(v) for v in input().split()]
a_list = [int(v) - 1 for v in input().split()]
l_list = [int(v) - 1 for v in input().split()]

cell_list = [-1] * (n)
for i, curr_koma in enumerate(a_list):
    cell_list[curr_koma] = i

for l in l_list:
    curr_koma = a_list[l]
    if cell_list[curr_koma] >= 0:
        # 末尾以外
        if len(cell_list) - 2 >= curr_koma:
            # 右にコマがなければ
            if cell_list[curr_koma + 1] == -1:
                cell_list[curr_koma + 1] = cell_list[curr_koma]
                cell_list[curr_koma] = -1
                a_list[l] += 1

ans = ""
for i, cell in enumerate(cell_list):
    if cell >= 0:
        ans += str(i + 1) + " "

print(ans)
