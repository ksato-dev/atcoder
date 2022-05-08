# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, k = [int(v) for v in input().split()]
    ab_dict = dict()

    for i in range(n):
        next_id, b = [int(v) for v in input().split()]
        if next_id not in ab_dict:
            ab_dict[next_id] = b
        else:
            ab_dict[next_id] += b

    a_list = sorted(ab_dict.keys())

    curr_id = 0
    for next_id in a_list:
        b = ab_dict[next_id]
        if next_id - curr_id > k:
            curr_id += k  # k だけ村を移動
            k = 0  # 使い果たしたので０
            break

        else:
            k -= (next_id - curr_id)  # 移動分だけ差し引く
            curr_id = next_id  # curr_id を更新
            k += b  # お金をもらう

    ans_id = curr_id + k  # 全部のお金もらった後に進める村まで進む
    print(ans_id)
