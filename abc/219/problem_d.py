import numpy as np
from numba import njit


@njit
def main(n, x, y, ab_list):
    inf = 1000

    # dp[i][j][k] :=（状態 (i,j,k) に達するまでに、高橋君が購入する弁当の個数の最小値）
    dp = np.full((n + 1, x + 1, y + 1), inf, dtype=np.int64)  # 型を間違えるとコケる

    dp[0, 0, 0] = 0
    for i in range(n + 1):
        if i == 0:
            continue
        for j in range(x + 1):
            for k in range(y + 1):
                pre_a = ab_list[i - 1][0]
                pre_b = ab_list[i - 1][1]
                dp[i, min(j + pre_a, x), min(k + pre_b, y)] = min(
                    dp[i, min(j + pre_a, x), min(k + pre_b, y)],
                    dp[i - 1, j, k] + 1
                )
                dp[i, j, k] = min(dp[i, j, k], dp[i - 1, j, k])

    ans = dp[n, x, y]
    if ans == inf:
        ans = -1
    print(ans)


if __name__ == "__main__":
    n = int(input())
    x, y = [int(v) for v in input().split()]

    ab_list = []
    max_sum_a = 0
    max_sum_b = 0
    for _ in range(n):
        a, b = [int(v) for v in input().split()]
        max_sum_a = max_sum_a + a
        max_sum_b = max_sum_b + b
        ab_list.append((a, b))

    main(n, x, y, ab_list)
