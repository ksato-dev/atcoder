import numpy as np


def check_odd(value):
    ret_flag = False
    if value % 2 == 1:
        ret_flag = True

    return ret_flag


if __name__ == "__main__":
    max_a = int(1e9)
    N = input()
    a_list = np.array([check_odd(int(v)) for v in input().split()])

    odd_sum = np.count_nonzero(a_list)

    if check_odd(odd_sum):
        print("NO")
    else:
        print("YES")
