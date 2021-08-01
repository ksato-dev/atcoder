def update_push_based_dp_sum(dp_sum, h_list, h_id, loop_num):
    max_h_id = len(dp_sum) - 1
    for i in range(loop_num):
        offset = i + 1
        if max_h_id - (h_id + offset) < 0:
            continue

        # 配る先と比較
        dp_sum[h_id + offset] = min(dp_sum[h_id + offset], abs(h_list[h_id + offset] - h_list[h_id]) + dp_sum[h_id])


if __name__ == "__main__":
    n, k = [int(v) for v in input().split()]
    h_list = [int(v) for v in input().split()]

    inf = int(10 ** 18)
    dp_sum = [inf] * n

    dp_sum[0] = 0
    for h_id in range(n):
        update_push_based_dp_sum(dp_sum, h_list, h_id, k)

    print(dp_sum[n - 1])
