if __name__ == "__main__":
    N, C, K = [int(value) for value in input().split()]
    time_list = [int(input()) for _ in range(N)]

    time_list.sort()

    p_cnt = 0
    start_time = 0
    count_buses = 0
    for curr_time in time_list:
        if p_cnt == 0:
            p_cnt += 1
            start_time = curr_time
            count_buses += 1
            continue

        if p_cnt < C and curr_time <= start_time + K:
            p_cnt += 1
        else:
            p_cnt = 1  # reset
            start_time = curr_time
            count_buses += 1

    print(count_buses)
