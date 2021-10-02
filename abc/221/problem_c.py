if __name__ == "__main__":
    n = input()
    n_list = list(n)
    # print(n_list)

    # 実装微妙
    max_prod = 0
    # bit search
    # 2個に分離
    num_of_digits = len(n)
    for dec_bits in range(2 ** num_of_digits):
        specified_digit = "0" + str(num_of_digits) + "b"
        bits_str = format(dec_bits, specified_digit)
        sum_bits = sum(map(int, list(bits_str)))
        if sum_bits == num_of_digits or sum_bits == 0:
            continue
        val1 = []
        val2 = []
        for arr_id, bit in enumerate(bits_str):
            curr_value = int(n[arr_id])
            if bit == "1":
                val1.append(curr_value)
            elif bit == "0":
                val2.append(curr_value)
        val1_sorted_str = None
        val2_sorted_str = None
        if len(val1) > 1:
            val1.sort(reverse=True)
            val1 = [str(v) for v in val1]
            val1_sorted_str = "".join(val1)
        else:
            val1_sorted_str = val1[0]
        if len(val2) > 1:
            val2.sort(reverse=True)
            val2 = [str(v) for v in val2]
            val2_sorted_str = "".join(val2)
        else:
            val2_sorted_str = val2[0]

        cand_max_prod = int(val1_sorted_str) * int(val2_sorted_str)
        if max_prod < cand_max_prod:
            max_prod = cand_max_prod

    print(max_prod)

