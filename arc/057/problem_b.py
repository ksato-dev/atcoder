import numpy as np

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    a_list = []

    for _ in range(n):
        a_list.append(int(input()))

    # dp[i][j] = 0 ~ i 日目までに j 回ゲームを行ったとして、この期間で機嫌の良かった日数の最大値
    dp = np.zeros((n+1, k+1))

    for i in range(1, n):
        for j in range(0, a_list[i] + 1):
            curr_win_rate = j / sum(a_list[0:i])
            next_win_rate = (j + 1) / sum(a_list[0:i+1])
            if next_win_num <= k:
                dp[i+1][next_win_num] = max(dp[i][j] +
                                            next_win_num, dp[i+1][next_win_num])
    
