def check_odd(value):
    ret_flag = False
    if value % 2 == 1:
        ret_flag = True
    return ret_flag


if __name__ == "__main__":
    n = int(input())
    a_list = []
    for _ in range(n):
        a_list.append(int(input()))

    a_list.sort()

    is_on_paper = 0
    calling_cnt = 0
    bf_a = a_list[0]
    for arr_id, a in enumerate(a_list):
        if arr_id == 0:
            calling_cnt = 1
            bf_a = a
            continue

        diff = a - bf_a
        if diff == 0:
            calling_cnt = calling_cnt + 1
        else:
            if check_odd(calling_cnt):
                is_on_paper = is_on_paper + 1
            calling_cnt = 1

        if arr_id == len(a_list) - 1:
            if check_odd(calling_cnt):
                is_on_paper = is_on_paper + 1

        bf_a = a

    print(is_on_paper)
