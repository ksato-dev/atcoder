if __name__ == "__main__":
    n = int(input())
    inv_ope_str = ""
    while True:
        if n == 1:
            inv_ope_str += "A"
            break

        if n % 2 == 1:
            inv_ope_str += "A"
            n = n - 1
        else:
            inv_ope_str += "B"
            n = n // 2

    print(inv_ope_str[::-1])
