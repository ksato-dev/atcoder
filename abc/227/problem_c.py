if __name__ == "__main__":
    n = int(input())

    cnt = 0
    # これでも通るが間に合わない #1
    # for c in range(n, 0, -1):
    #     for b in range(c, 0, -1):
    #         for a in range(b, 0, -1):
    #             abc = a * b * c
    #             if abc <= n:
    #                 cnt = cnt + 1

    # a, b, c の最大値を考えて全探索
    # これでも通るが間に合わない #2
    # a_max = int(pow(n, 1/3))
    # for a in range(1, a_max + 1):
    #     b_max = int(pow(n/a, 1/2))
    #     for b in range(a, b_max + 1):
    #         c_max = int(n / (a * b))
    #         for c in range(b, c_max + 1):
    #             abc = a * b * c
    #             if abc <= n:
    #                 cnt = cnt + 1

    # # #2 の高速化版
    # a_max = int(pow(n, 1/3))
    # for a in range(1, a_max + 1):
    #     b_max = int(pow(n/a, 1/2))
    #     for b in range(a, b_max + 1):
    #         c_max = int(n / (a * b))
    #         c_range = c_max - b + 1
    #         cnt = cnt + c_range

    # #2 の高速化版 #2
    # pow 関数でやろうとすると誤差のせいなのか WA が出る。
    for a in range(1, n + 1):
        if a * a * a > n:
            break
        for b in range(a, n + 1):
            if a * b * b > n:
                break
            c_max = int(n / (a * b))
            c_range = c_max - b + 1
            cnt = cnt + c_range

    print(cnt)
