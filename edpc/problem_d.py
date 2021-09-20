import numpy as np
from numba import njit


@njit
def main(n, tgt_w, wv_list):

    # dp[i][sum_w] := 品物を番号 0 から i-1 までそれぞれ選択するしないをして、
    # 重さが w になったときの価値の最大値を保存する。
    dp = np.zeros((n + 1, tgt_w + 1), dtype=np.int64)
    # v0 = wv_list[0][1]
    # w0 = wv_list[0][0]
    # dp[0][w0] = v0

    for i in range(n):
        for sum_w in range(tgt_w + 1):
            w_i, v_i = wv_list[i]
            if sum_w >= w_i:
                # 選ぶ場合
                dp[i + 1, sum_w] = max(dp[i, sum_w - w_i] +
                                       v_i, dp[i + 1, sum_w])

            # 選ばない場合
            dp[i + 1, sum_w] = max(dp[i, sum_w], dp[i + 1, sum_w])

    print(dp[n, tgt_w])


if __name__ == "__main__":
    n, tgt_w = [int(v) for v in input().split()]
    wv_list = []
    for _ in range(n):
        w, v = [int(v) for v in input().split()]
        wv_list.append((w, v))

    main(n, tgt_w, wv_list)
