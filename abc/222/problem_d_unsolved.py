import numpy as np
from numba import njit

@njit
def main(n, day_info_list):
    cnt_list = np.array([0] * (10 ** 9))
    for d_id in range(n):
        start_day = day_info_list[d_id][0]
        period = day_info_list[d_id][1]
        cnt_list[start_day:start_day+period] += 1

    # print(cnt_list)
    for day in range(n):
        print(np.sum(cnt_list == day+1))


if __name__ == "__main__":
    n = int(input())
    day_info_list = []
    for _ in range(n):
        start_day, period = [int(v) for v in input().split()]
        day_info_list.append((start_day, period))

    main(n, day_info_list)
