import numpy as np
# from numba import njit


# @njit
def execute(tgt_w, item_list, dp):
    n = dp.shape[0]
    for item_id in range(1, n):
        value = item_list[item_id][0]
        weight = item_list[item_id][1]
        for w in range(tgt_w + 1):
            curr_value = None
            # 今の品物を選ぶ
            if w >= weight:
                curr_value = dp[item_id - 1, w - weight] + value
                dp[item_id, w] = max(dp[item_id, w], curr_value)

            # 今の品物を選ばない
            curr_value = dp[item_id - 1, w]
            dp[item_id, w] = max(dp[item_id, w], curr_value)

    # print(dp)
    res = int(np.amax(dp[:, tgt_w]))
    print(res)


if __name__ == "__main__":
    n, tgt_w = [int(v) for v in input().split()]
    item_list = [(None, None)]
    for _ in range(n):
        value, weight = [int(v) for v in input().split()]
        item_list.append((value, weight))

    # dp[i][w] := 重さ w 未満になるように 0~i まで品物を選んだときの value の最大値
    dp = np.zeros((n + 1, tgt_w + 1))

    execute(tgt_w, item_list, dp)
