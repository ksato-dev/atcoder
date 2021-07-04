import math


def read_data():
    line = input()
    ret_data = int(line)

    return ret_data


def F(A, B):
    A_digit = len(str(A))
    B_digit = len(str(B))
    return max(A_digit, B_digit)


if __name__ == "__main__":
    N = read_data()

    min_digit = 1e20
    for a in range(1, int(math.sqrt(N)) + 1):
        remainder = N % a
        if remainder != 0:
            continue
        b = N / a
        digit = F(int(a), int(b))
        min_digit = min(digit, min_digit)

    print(min_digit)
