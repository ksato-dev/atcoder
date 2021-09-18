if __name__ == "__main__":
    n = int(input())
    h_list = [int(v) for v in input().split()]
    inf = int(10 ** 18)

    if n == 2:
        ans_n2 = abs(h_list[1] - h_list[0])
        print(ans_n2)
        exit()

    # dp[i] := カエルが足場 i に到達するまでに必要な最初コスト
    dp = [inf] * n
    dp[0] = 0
    dp[1] = abs(h_list[1] - h_list[0])
    dp[2] = abs(h_list[2] - h_list[0])

    for i in range(n):
        if i < 3:
            continue
        dp1 = dp[i-1] + abs(h_list[i] - h_list[i-1])
        dp2 = dp[i-2] + abs(h_list[i] - h_list[i-2])
        dp[i] = min(dp1, dp2)

    print(dp[n-1])
