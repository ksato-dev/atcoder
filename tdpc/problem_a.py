if __name__ == "__main__":
    n = int(input())
    p_list = [int(v) for v in input().split()]
    p_max = sum(p_list)

    # dp[i][p] := 0~i 番目の品物を使って p を作れるかどうか
    # dp[0][0] = True
    # dp[0][1:] = False
    dp = [None] * (n + 1)
    for n_id in range(n + 1):
        dp[n_id] = [False] * (p_max + 1)

    dp[0][0] = True
    for n_id in range(n + 1):
        if n_id == 0:
            continue
        for p in range(p_max + 1):
            if not dp[n_id - 1][p]:
                continue
            dp[n_id][p] = True  # 一つ前の問題までで p まで表せるなら、ここでも p まで表せる。

            p_sum = p + p_list[n_id - 1]
            if p_sum <= p_max:  # テーブルに埋めることができるか
                dp[n_id][p_sum] = True

    # dp テーブルの列成分について、OR 演算をする。
    cnt = 0
    for p in range(p_max + 1):
        col_data = [row_data[p] for row_data in dp]
        if any(col_data):
            cnt = cnt + 1

    print(cnt)
