import numpy as np
from numba import njit


@njit
def main(n, k, h_list, inf):
    """
    もらう DP の方が書きやすそう
    """

    # dp[i] := 足場 i に到達するまでに必要な最小コスト
    dp = [inf] * n

    if n < k:
        for i in range(n):
            dp[i] = abs(h_list[i] - h_list[0])
        print(dp[n-1])
        return

    # initialize
    for i in range(k):
        dp[i] = abs(h_list[i] - h_list[0])

    for i in range(n):
        if i < k:
            continue
        for j in range(1, k+1):
            cand_dp = abs(h_list[i] - h_list[i-j]) + dp[i-j]
            dp[i] = min(dp[i], cand_dp)

    print(dp[n-1])


if __name__ == "__main__":
    n, k = [int(v) for v in input().split()]
    h_list = np.array([int(v) for v in input().split()], dtype=np.int64)
    inf = int(10 ** 18)
    main(n, k, h_list, inf)
