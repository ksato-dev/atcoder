# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    a_list = [int(v) for v in input().split()]
    b_list = [int(v) for v in input().split()]
    c_list = [int(v) for v in input().split()]

    ans = 0
    # 間に合わない
    for i in range(n):
        a_i = a_list[i]
        for j in range(n):
            c_j = c_list[j]
            b_cj = b_list[c_j-1]

            if a_i == b_cj:
                ans += 1

    print(ans)
