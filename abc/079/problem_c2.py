def formula_str_2_value(formula_str):
    result = int(formula_str[0])
    size_str = len(formula_str)
    for c_id in range(1, size_str, 2):
        result = result + int(formula_str[c_id:c_id+2])
    return result


if __name__ == "__main__":
    abcd = input()
    n = len(abcd)

    # bit-searching
    # 0:="-", 1:="+"
    for bits in range(2**(n-1)):
        specified_digits = "0" + str(n-1) + "b"
        bits_str = format(bits, specified_digits)
        # print(bits_str)

        curr_formula_str = abcd[0]
        for c_id, bit in enumerate(bits_str):
            ope = None
            if bit == "1":
                ope = "+"
            else:
                ope = "-"

            curr_formula_str = curr_formula_str + ope + abcd[c_id + 1]

        if formula_str_2_value(curr_formula_str) == 7:
            print(curr_formula_str + "=7")
            exit()
