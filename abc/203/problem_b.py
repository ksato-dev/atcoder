# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, k = [int(v) for v in input().split()]

    sum_ans = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum_ans += 100 * i + j

    print(sum_ans)
