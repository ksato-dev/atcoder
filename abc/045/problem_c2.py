if __name__ == "__main__":
    s = input()
    n = len(s)

    total_sum = 0
    for bits in range(2**(n-1)):
        specified_digit = "0" + str(n-1) + "b"
        bits_str = format(bits, specified_digit)

        curr_sum_str = s[0]
        for digit in range(0, n-1):
            if int(bits_str[digit]):
                curr_sum_str = curr_sum_str + "+" + s[digit + 1]
            else:
                curr_sum_str = curr_sum_str + s[digit + 1]

        total_sum = total_sum + sum(map(int, curr_sum_str.split("+")))

    print(total_sum)
