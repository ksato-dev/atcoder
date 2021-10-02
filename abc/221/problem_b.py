if __name__ == "__main__":
    s = input()
    t = input()

    not_match_cnt = 0
    not_match_char_list = []
    for arr_id, val in enumerate(zip(s, t)):
        s_c = val[0]
        t_c = val[1]
        if not s_c == t_c:
            not_match_cnt += 1
            not_match_char_list.append((arr_id, val))

    if not_match_cnt == 2:
        pair0 = not_match_char_list[0]
        pair1 = not_match_char_list[1]
        if abs(pair0[0] - pair1[0]) == 1:
            if pair0[1][0] == pair1[1][1] and pair0[1][1] == pair1[1][0]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    elif not_match_cnt == 0:
        print("Yes")
    else:
        print("No")
