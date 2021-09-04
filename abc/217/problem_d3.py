import numpy as np

if __name__ == "__main__":
    l, q = [int(v) for v in input().split()]

    bar_range_list = [(0, l)]
    bar_list = np.array([l] * (2 * l))  # 0 ~ l
    ans_list = []
    for _ in range(q):
        q, value = [int(v) for v in input().split()]
        value = value
        if q == 1:
            for b_id, bar_bounds in enumerate(bar_range_list):
                bar_s = bar_bounds[0]
                bar_e = bar_bounds[1]
                if bar_s < value < bar_e:
                    bar_range_list.pop(b_id)
                    bar_range_list.append((bar_s, value))
                    bar_range_list.append((value, bar_e))
                    # bar_list[value] = 0
                    bar_list[bar_s:value] = value - bar_s
                    bar_list[value:bar_e] = bar_e - value
                    break

        elif q == 2:
            ans_list.append(bar_list[value])

    for ans in ans_list:
        print(ans)