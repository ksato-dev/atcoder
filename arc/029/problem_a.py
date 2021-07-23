if __name__ == "__main__":
    n = int(input())
    t_list = [int(input()) for _ in range(n)]

    min_total_time = 100000
    for dec_num in range(2**n):
        bin_digits = "0" + str(n) + "b"
        bin_num = format(dec_num, bin_digits)

        sum_a = 0
        sum_b = 0
        for digit_id, bit in enumerate(bin_num):

            if bit == "1":
                sum_a = sum_a + t_list[digit_id]
            else:
                sum_b = sum_b + t_list[digit_id]

        if sum_a > sum_b:
            total_time = sum_a
        else:
            total_time = sum_b

        if total_time < min_total_time:
            min_total_time = total_time

    print(min_total_time)
