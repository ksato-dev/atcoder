def calc_formula(formula):
    array = map(int, formula.split("+"))
    array = list(array)
    answer = 0
    for a_id in range(len(array)):
        if (a_id == 0):
            answer = array[0]
            continue
        answer = answer + array[a_id]

    return answer


if __name__ == "__main__":
    s = input()
    n = len(s)

    total_sum = 0
    for dec_num in range(2**n):
        bin_digits = "0" + str(n) + "b"
        bin_num = format(dec_num, bin_digits)

        formula = ""
        for b_id, bit in enumerate(bin_num):
            if bit == "1":
                formula = formula + "+"

            formula = formula + s[b_id]

        # 先頭ビットが１のときは計算しない
        if formula[0] == "+":
            continue

        total_sum = total_sum + calc_formula(formula)
    print(total_sum)
