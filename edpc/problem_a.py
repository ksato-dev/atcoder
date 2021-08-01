if __name__ == "__main__":
    n = int(input())
    h_list = [int(v) for v in input().split()]

    inf = int(10 ** 18)
    dp_sum = [inf] * n

    # もらう DP でやる。
    for h_id in range(n):
        if h_id == 0:
            dp_sum[h_id] = 0
        elif h_id == 1:
            dp_sum[h_id] = abs(h_list[h_id] - h_list[h_id - 1])
        else:
            cand_dp_sum1 = abs(
                h_list[h_id] - h_list[h_id - 1]) + dp_sum[h_id - 1]
            cand_dp_sum2 = abs(
                h_list[h_id] - h_list[h_id - 2]) + dp_sum[h_id - 2]
            dp_sum[h_id] = min(cand_dp_sum1, cand_dp_sum2)

    print(dp_sum[n-1])
