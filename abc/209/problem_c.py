if __name__ == "__main__":
    inf_val = int(1e9) + 7
    max_n = (2 * 1e5)
    n = int(input())
    c_list = [int(v) for v in input().split()]
    c_list.sort()

    is_a_list = True
    count_a_list = 1
    for arr_id, c in enumerate(c_list):
        diff = c - arr_id
        if diff <= 0:
            is_a_list = False
            break
        else:
            count_a_list *= diff

        if arr_id > max_n:
            break

    if is_a_list:
        print(count_a_list)
        print(count_a_list % inf_val)
    else:
        print(0)
