if __name__ == "__main__":
    l, q = [int(v) for v in input().split()]

    bar_list = [(0, l)]
    for _ in range(q):
        q, value = [int(v) for v in input().split()]
        if q == 1:
            for b_id, bar_bounds in enumerate(bar_list):
                bar_s = bar_bounds[0]
                bar_e = bar_bounds[1]
                if bar_s < value < bar_e:
                    bar_list.pop(b_id)
                    bar_list.append((bar_s, value))
                    bar_list.append((value, bar_e))
                    break

        elif q == 2:
            for bar_bounds in bar_list:
                bar_s = bar_bounds[0]
                bar_e = bar_bounds[1]
                if bar_s < value < bar_e:
                    print(bar_e - bar_s)
                    break
