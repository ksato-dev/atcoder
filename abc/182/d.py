n = int(input())
a_list = [int(v) for v in input().split()]

a_rs = [0] * (n + 1)
max_step = [0] * n  # i の操作中に最も正の方向へ進んだときの値
max_a_rs = 0
for i in range(1, n + 1):
    a_rs[i] = a_list[i - 1] + a_rs[i - 1]
    curr_step_sum = a_rs[i] - a_rs[0]
    if max_a_rs < curr_step_sum:
        max_a_rs = curr_step_sum
    max_step[i - 1] = max_a_rs

max_pos = (-1) * (10 ** 10)
pos = 0
for i in range(n):
    # max_step[i] を活用して、現在の操作における最大位置を調べる。
    if max_pos < pos + max_step[i]:
        max_pos = pos + max_step[i]
    pos += (a_rs[i + 1] - a_rs[0])

print(max_pos)
