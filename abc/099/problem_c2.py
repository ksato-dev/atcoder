import numpy as np

if __name__ == "__main__":
    n = int(input())

    cnt = 0
    # remainder_9 = 0
    # if 9 < n:
    #     remainder_9 = n % 9

    if 9 < n:
        pow9 = 9
        cnt = cnt + 1
        while pow9 < n:
            pow9 = pow9 * 9
            cnt = cnt + 1
        # pow9 = pow9 / 9
        # cnt = cnt - 1
        n = n - pow9

    if 0 < n < 6:
        cnt = cnt + n
    elif 6 <= n:
        cnt = 1 + (n - 6)

    print(cnt)
