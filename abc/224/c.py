# -*- coding: utf-8 -*-

def judge_plus_triangle(a, b, c, d, e, f):
    # なんか知らんけど、積分してマイナスのときもプラスと考えるらしい。
    # ret_is_plus = (a * d + c * f + e * b - b * c - d * e - f * a) > 0
    ret_is_plus = (c - a) * (f - b) != (e - a) * (d - b)
    return ret_is_plus


n = int(input())

xy_list = list()
for i in range(n):
    x, y = [int(v) for v in input().split()]
    xy_list.append((x, y))


cnt_plus_area = 0
for i in range(n):
    x1, y1 = xy_list[i]
    for j in range(i + 1, n):
        x2, y2 = xy_list[j]
        for k in range(j + 1, n):
            x3, y3 = xy_list[k]

            if judge_plus_triangle(x1, y1, x2, y2, x3, y3):
                cnt_plus_area += 1

# 同じ組み合わせが３回出るので３で割る。
print(cnt_plus_area)
# print(cnt)
