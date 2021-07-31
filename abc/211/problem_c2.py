import numpy as np


if __name__ == "__main__":
    src_str = input()
    tgt_str = "chokudai"
    i_max = len(src_str) + 1
    j_max = len(tgt_str) + 1
    dp = [[0] * j_max for _ in range(i_max)]
    # dp = np.array(dp, dtype=np.int) # 何故か numpy だと解けなかった。
    for i in range(i_max):
        dp[i][0] = 1

    for i in range(i_max):
        if i == 0:
            continue
        for j in range(j_max):
            if j == 0:
                continue
            # 文字列の参照は１ずらす
            dp[i][j] = dp[i-1][j]
            if src_str[i - 1] == tgt_str[j - 1]:
                dp[i][j] = dp[i][j] + dp[i-1][j-1]

    print(dp[-1][-1] % (10**9 + 7))
