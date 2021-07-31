def binary_search(sorted_list, search_value) -> bool:
    left_index: int = 0
    right_index: int = len(sorted_list) - 1
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = sorted_list[middle_index]

        if search_value < middle_value:
            right_index = middle_index - 1
            continue
        if search_value > middle_value:
            left_index = middle_index + 1
            continue

        return (True, left_index, right_index)

    return (False, left_index, right_index)


if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]
    b_list = [int(v) for v in input().split()]

    a_list.sort()
    b_list.sort()

    bin_search_tgt = None
    bin_size = None
    linear_search_tgt = None
    if n > m:
        bin_search_tgt = a_list
        bin_size = n
        linear_search_tgt = b_list
    else:
        bin_search_tgt = b_list
        bin_size = m
        linear_search_tgt = a_list

    inf = int(1e12)
    min_diff = inf
    for x in linear_search_tgt:
        tgt_res = binary_search(bin_search_tgt, x)
        if tgt_res[0]:
            print(0)
            exit()
        else:
            y_id1 = tgt_res[1]
            y_id2 = tgt_res[2]
            if 0 <= y_id1 < bin_size:
                diff1 = abs(x - bin_search_tgt[y_id1])
            else:
                diff1 = inf
            if 0 <= y_id2 < bin_size:
                diff2 = abs(x - bin_search_tgt[tgt_res[2]])
            else:
                diff2 = inf

            if diff1 < diff2:
                if min_diff > diff1:
                    min_diff = diff1
            else:
                if min_diff > diff2:
                    min_diff = diff2

    print(min_diff)
