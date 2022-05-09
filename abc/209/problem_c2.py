# -*- coding: utf-8 -*-

def main():
    n = int(input())
    c_list = [int(v) for v in input().split()]
    c_list.sort()

    ans = 1
    for i in range(n):
        # 順列の考え方で積算する。
        ans = ans * (c_list[i]-i)  # 一つ前より選択肢が一つ減る。
    print(ans % (10**9+7))


if __name__ == "__main__":
    main()
