if __name__ == "__main__":
    l, q = [int(v) for v in input().split()]

    bar_list = [l] * (l+1)  # 0 ~ l
    for _ in range(q):
        q, value = [int(v) for v in input().split()]
        if q == 1:
            # bar_list[value] = False
            bar_list[]

        elif q == 2:
            start_id = None
            for l_id in range(value, -1, -1):
                if not bar_list[l_id]:
                    start_id = l_id                   
                    break
            end_id = None
            for l_id in range(value, l + 1):
                if not bar_list[l_id]:
                    end_id = l_id                   
                    break
            print(end_id - start_id)
