# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # 配列作ると無理なので、作らずに二分探索をやる。
    x, a, d, n = [int(v) for v in input().split()]

    # 交差 d がマイナスの時、数列が反転して取り扱いにくいので、正規化する。
    if d < 0:
        a = a + d * (n - 1)  # 末尾の項を初項にする。
        d *= -1

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = a + mid * d
        if mid_value < x:
            left = mid + 1
        else:
            right = mid - 1

    ans_value = 10 ** 19
    for i in range(-5, 6):
        id = max(left + i, 0)
        id = min(id, n-1)
        ans_value = min(abs(a + id * d - x), ans_value)

    print(ans_value)
