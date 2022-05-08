# -*- coding: utf-8 -*-

if __name__ == "__main__":
    val_list = map(int, input().split())
    cnt_list = [0] * (6+1)

    for val in val_list:
        cnt_list[val] += 1

    two_value_is_same = False
    ans = 0
    for c_id, cnt in enumerate(cnt_list):
        if cnt == 3:
            ans = c_id
            break
        elif cnt == 2:
            two_value_is_same = True

    if two_value_is_same:
        for c_id, cnt in enumerate(cnt_list):
            if cnt == 1:
                ans = c_id
                break

    print(ans)
