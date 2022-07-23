# -*- coding: utf-8 -*-


def main():
    n, m = [int(v) for v in input().split()]
    x_list = [int(v) for v in input().split()]
    cy_dict = dict()

    for i in range(m):
        c, y = [int(v) for v in input().split()]
        cy_dict[c] = y

    # dp[i][j] := i 回のコイントス（0~i-1）で得られた報酬の最大値
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    dp[0] = [0] * (n + 1)

    # 配る DP
    for i in range(n):
        x = x_list[i]

        for j in range(i + 1):
            if dp[i][j] == -1:
                continue

            y = 0
            # 裏
            dp[i + 1][0] = max(dp[i][j], dp[i + 1][0])

            # 表
            if j + 1 in cy_dict:
                y = cy_dict[j + 1]
            dp[i + 1][j + 1] = max(dp[i][j] + x + y, dp[i + 1][j + 1])


    max_val = max(list(map(lambda x: max(x), dp)))
    print(max_val)


if __name__ == "__main__":
    main()
