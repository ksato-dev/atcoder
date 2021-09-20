import numpy as np

if __name__ == "__main__":
    n = int(input())

    # dp[i] := i 円引き出すのに必要な最小引き出し回数
    inf = n + 1000
    dp = np.full(n+1, inf)
    dp[0] = 0

    # 方針：はじめに 9 ** m で割り切れるかどうか見て、次に 6 ** m で割り切れるか見て、
    # 最後の余りを 1 での引き出し回数とする。

    for i in range(n+1):

        # i - pow6 -> i の遷移を調べる。
        pow6 = 1  # 1 スタートにすると 1 を引き出す操作も表現できる。
        while True:
            if i < pow6:
                break
            dp[i] = min(dp[i - pow6] + 1, dp[i])
            pow6 = pow6 * 6

        # i - pow9 -> i の遷移を調べる。
        pow9 = 1
        while True:
            if i < pow9:
                break
            dp[i] = min(dp[i - pow9] + 1, dp[i])
            pow9 = pow9 * 9

    print(dp[n])
