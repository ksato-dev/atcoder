import numpy as np
from numba import njit


@njit
def main(n, k, h_list, inf):
    """
    配る DP で書いてみる。
    余裕を持って配列を確保すると、配る DP で書きやすい。
    """

    # dp[i] := 足場 i に到達するまでに必要な最小コスト
    dp = [inf] * (n + k)

    # initialize
    dp[0] = 0

    # calculate
    for i in range(n):
        for j in range(1, k+1):
            cand_dp = dp[i] + abs(h_list[i+j] - h_list[i])
            dp[i+j] = min(dp[i+j], cand_dp)

    print(dp[n-1])


if __name__ == "__main__":
    n, k = [int(v) for v in input().split()]
    pre_h_list = [int(v) for v in input().split()]
    pre_h_list.extend([0] * k)
    h_list = np.array(pre_h_list, dtype=np.int64)
    inf = int(10 ** 18)
    main(n, k, h_list, inf)
