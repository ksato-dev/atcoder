# -*- coding:utf-8 -*-
# link: https://atcoder.jp/contests/abc215/tasks/abc215_d


def factorization(n):
    """nを素因数分解"""
    """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
    arr = []
    # arr = set()
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            # cnt = 0
            while temp % i == 0:
                # cnt += 1
                temp //= i
            # arr.append([i, cnt])
            arr.append(i)

    if temp != 1:
        # arr.append([temp, 1])
        arr.append(temp)

    if arr == []:
        # arr.append([n, 1])
        arr.append(n)

    return arr


if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]
    a_list = list(set(a_list))

    # a の素因数の倍数を k の候補から消すと答えが出る。
    # 素因数間の交差を考える。
    ans_k_list = [1]
    k_list = [i for i in range(2, m + 1)]
    for k in k_list:
        set_of_k_factors = set(factorization(k))

        intersect_any = False
        for a in a_list:
            if a == 1:
                continue
            set_of_a_factors = set(factorization(a))
            if set_of_k_factors & set_of_a_factors:
                intersect_any = True

        if not intersect_any:
            ans_k_list.append(k)

    print(len(ans_k_list))
    for k in ans_k_list:
        print(k)
