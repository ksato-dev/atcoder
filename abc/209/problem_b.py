if __name__ == "__main__":
    n, x = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]

    sum_a = 0
    for arr_id, a in enumerate(a_list):
        if ((arr_id + 1) % 2 == 0):
            sum_a += a - 1
        else:
            sum_a += a

    if sum_a <= x:
        print("Yes")
    else:
        print("No")
