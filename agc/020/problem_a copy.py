def check_odd(value):
    ret_flag = False
    if value % 2 == 1:
        ret_flag = True

    return ret_flag


if __name__ == "__main__":
    n, a, b = [check_odd(int(v)) for v in input().split()]

    if check_odd(a - b):
        print("Borys")
    else:
        print("Alice")
