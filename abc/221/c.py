
n_str = input()
n = int(n_str)
n_digits = len(n_str)

max_product_result = 0
for bits_dec in range(2 ** n_digits):
    specified_digits = "0" + str(n_digits) + "b"
    bits_str = format(bits_dec, specified_digits)
    # 全部同じ時飛ばす。
    if (bits_str == "0" * n_digits or bits_str == "1" * n_digits):
        continue

    elems0 = []
    elems1 = []

    # 左からビット数を見ていく。
    for i, bit in enumerate(bits_str):
        digit_num = n_digits - i
        if bit == "0":
            elems0.append(n_str[digit_num - 1])
        elif bit == "1":
            elems1.append(n_str[digit_num - 1])

    # 降順にソート
    elems0.sort(reverse=True)
    elems1.sort(reverse=True)
    elems0_str = [str(v) for v in elems0]
    elems1_str = [str(v) for v in elems1]

    # print(elems0_str, elems1_str)

    value0 = int("".join(elems0_str))
    value1 = int("".join(elems1_str))

    # print(value0, value1)
    product_result = value0 * value1
    if max_product_result < product_result:
        max_product_result = product_result

print(max_product_result)
