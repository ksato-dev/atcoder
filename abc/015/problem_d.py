import numpy as np
from numba import njit


@njit
def main(W, N, K, ab_list):

    # dp[i][j][k] := i 枚目までのスクリーンショットを使って j 枚まで貼ったとして
    # 幅 k にしたときの重要度の最大値
    dp = np.zeros((N+1, K+1, W+1), dtype=np.int32)

    for i in range(N):
        a, b = ab_list[i]
        for j in range(K + 1):
            if j == K:
                continue  # これ以上選択できない

            for k in range(W + 1):
                if a + k <= W:
                    # 選んだとき
                    dp[i+1][j+1][k+a] = max(dp[i+1]
                                              [j+1][k+a], dp[i][j][k] + b)
                # 選ばなかったとき
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

    # print(dp[N][K][W])
    print(np.max(dp))


if __name__ == "__main__":
    W = int(input())
    N, K = [int(v) for v in input().split()]
    ab_list = []
    for _ in range(N):
        a, b = [int(v) for v in input().split()]
        ab_list.append((a, b))
    main(W, N, K, ab_list)
