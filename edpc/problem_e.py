import numpy as np
from numba import njit


@njit
def main(n, tgt_w, wv_list):

    # dp[i][sum_v] := 品物を番号 0 から i-1 までそれぞれ選択するしないをして、
    # 価値が sum_v になったときに持っている品物の重さの最小値を保存する。
    max_v = 100100  # sum(v) -> n * v_i_max になるので、100 * 10^3 で考える。
    inf = 10 ** 11
    dp = np.full((n+1, max_v), inf, dtype=np.int64)
    dp[0, 0] = 0  # 初期条件わからん。dp[0, w] = 0 じゃダメっぽい？

    for i in range(n):
        for sum_v in range(max_v):
            w_i, v_i = wv_list[i]
            # sum_w = dp[i][sum_v - v_i] + w_i
            if sum_v - v_i >= 0:
                # 選ぶ場合
                dp[i+1, sum_v] = min(dp[i, sum_v - v_i] + w_i, dp[i+1, sum_v])

            # 選ばない場合
            dp[i+1, sum_v] = min(dp[i, sum_v], dp[i+1, sum_v])

    tgt_v = 0
    for sum_v in range(max_v):
        if tgt_w >= dp[n, sum_v]:
            tgt_v = max(sum_v, tgt_v)

    print(tgt_v)


if __name__ == "__main__":
    n, tgt_w = [int(v) for v in input().split()]
    wv_list = []
    for _ in range(n):
        w, v = [int(v) for v in input().split()]
        wv_list.append((w, v))

    main(n, tgt_w, wv_list)
