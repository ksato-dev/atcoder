if __name__ == "__main__":
    n = int(input())
    a_matrix = [None] * 2
    a_matrix[0] = [int(a) for a in input().split()]
    a_matrix[1] = [int(a) for a in input().split()]

    # dp[i][j] := (i, j) における報酬の最大値
    dp = [None] * 2
    dp[0] = [-1] * n
    dp[1] = [-1] * n

    dp[0][0] = a_matrix[0][0]
    for c_1j in range(2):
        for c_2j in range(n):
            # move to right
            if c_2j < n - 1:
                new_dp = dp[c_1j][c_2j] + a_matrix[c_1j][c_2j + 1]
                dp[c_1j][c_2j + 1] = max(dp[c_1j][c_2j + 1], new_dp)

            # move down
            if c_1j == 0:
                new_dp = dp[c_1j][c_2j] + a_matrix[c_1j + 1][c_2j]
                dp[c_1j + 1][c_2j] = max(dp[c_1j + 1][c_2j], new_dp)

    print(dp[-1][-1])
