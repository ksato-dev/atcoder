# -*- coding: utf-8 -*-
# 解き直し

if __name__ == "__main__":
    # imos method で解く。

    n = int(input())

    # 区間の立ち上がり (l) と立ち下がり (r) をテーブルに登録。
    max_pos = 2 * 10 ** 5 + 10
    table = [0] * max_pos
    for i in range(n):
        l, r = [int(v) for v in input().split()]
        table[l] += 1
        table[r] += -1

    # 山（区間）になっている部分の両端を調べる。
    sum_value = 0
    pre_sum_value = 0
    section_list = list()
    for i in range(max_pos):
        value = table[i]
        sum_value += value  # 重ねていく。sum_value がゼロじゃなければ山がある。

        # (0 -> plus_value) の立ち上がり
        if sum_value > 0 and pre_sum_value == 0:
            section_list.append([i, i])  # [l, r] を登録。r はまだ不明なのでダミーを与える。

        # (plus_value -> 0) の立ち下がり
        if sum_value == 0 and pre_sum_value > 0:
            last_section_id = len(section_list) - 1
            section_list[last_section_id][1] = i  # ここで r を更新。

        pre_sum_value = sum_value

    for section in section_list:
        l = section[0]
        r = section[1]
        print(l, r)
