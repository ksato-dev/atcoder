def calc(formula):
    sum_data = int(formula[0])
    n = len(formula)
    for c_id in range(1, n, 2):
        value = formula[c_id:c_id+2]
        sum_data += int(value)
    return sum_data


def recursive_check(s, id, formula):
    n = len(s)

    if n - id == 1:
        result = calc(formula)
        if result == 7:
            print(formula + "=7")
            exit()
        return

    recursive_check(s, id + 1, formula + "+" + s[id + 1])
    recursive_check(s, id + 1, formula + "-" + s[id + 1])


if __name__ == "__main__":
    abcd = input()

    recursive_check(abcd, id=0, formula=abcd[0])
