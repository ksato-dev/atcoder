def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]
    a_list = list(set(a_list))
    a_max = max(a_list)

    k_list = [1]
    for k in range(1, m+1):
        all_gcd_is_1 = True
        for a in a_list:
            if gcd(a, k) != 1:
                all_gcd_is_1 = False
                break
        if not all_gcd_is_1:
            continue

        k_list.append(k)

    print(len(k_list))
    for k in k_list:
        print(k)
