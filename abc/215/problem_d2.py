# -*- coding:utf-8 -*-
# link: https://atcoder.jp/contests/abc215/tasks/abc215_d

import math


def get_set_of_prime_nums(n):
    if n < 2:
        return []
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]
    max_a = max(a_list)
    primes_is_max_a_or_less = get_set_of_prime_nums(max_a)

    k_flags = [True for _ in range(m + 1)]
    k_flags[0] = False
    # a の素因数の倍数を k の候補から消す。
    for a in a_list:
        if a == 1:
            continue
        k_flags[a] = False

    for prime in primes_is_max_a_or_less:
        for ignore_k in range(prime, m + 1, prime):
            k_flags[ignore_k] = False

    ans_k_list = [1]
    # k_append = ans_k_list.append
    for k in range(2, m + 1):
        if k_flags[k]:
            ans_k_list.append(k)

    print(len(ans_k_list))
    for k in ans_k_list:
        print(k)
