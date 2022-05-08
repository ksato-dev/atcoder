# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    a_list = [int(v) for v in input().split()]
    b_list = [int(v) for v in input().split()]
    c_list = [int(v) for v in input().split()]

    # 予め Ai と Bcj の値として考えられるものを全て列挙し、カウントする。（バケット法）
    a_cnt_list = [0] * (n+1)
    b_cnt_list = [0] * (n+1)
    for i in range(n):
        a_i = a_list[i]
        a_cnt_list[a_i] += 1

        c_i = c_list[i] - 1
        b_ci = b_list[c_i]
        b_cnt_list[b_ci] += 1

    ans_cnt = 0
    # 値が一致する A と B だけを調べる。
    for a_cnt, b_cnt in zip(a_cnt_list, b_cnt_list):
        if a_cnt * b_cnt:
            ans_cnt += a_cnt * b_cnt

    print(ans_cnt)
