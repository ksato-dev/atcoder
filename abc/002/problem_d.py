import itertools

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]

    if n == 1 or m == 0:
        print(1)
        exit()

    xy_list = [list(map(int, input().split())) for _ in range(m)]
    # print(xy_list)
    max_cnt = -1

    for bits in range(2**(n)):
        specified_digit = "0" + str(n) + "b"
        bits_str = format(bits, specified_digit)

        # bit = 1 の ID だけ取ってリスト化
        faction_people = [int(p_id + 1)
                          for p_id, exist in enumerate(bits_str) if exist == "1"]
        if (len(faction_people) < 2):
            continue

        # print("bits:", bits_str)
        # print("faction_people:", faction_people)

        combs = itertools.combinations(faction_people, 2)
        comb_list = list(combs)
        # print(comb_list)

        # もう少しきれいに書きたい。
        match_all_combs = True  # 全組み合わせが入力（x, y）と一致するか
        for comb in comb_list:
            match_comb = False
            for xy in xy_list:
                match_xy = xy[0] in comb and xy[1] in comb
                if match_xy:
                    match_comb = True  # マッチするものが一個でもあればよい

            if not match_comb:
                match_all_combs = False

        if match_all_combs:
            sum_1 = sum([int(bit) for bit in bits_str])
            if sum_1 > max_cnt:
                max_cnt = sum_1

    print(max_cnt)
