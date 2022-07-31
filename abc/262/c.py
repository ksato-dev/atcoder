# -*- coding: utf-8 -*-
def main():
    n = int(input())
    a_list = [int(v) - 1 for v in input().split()]

    ans = 0
    # i = a_i, j = a_j の時
    # a_i = i である個数を n として、n(n-1)//2 だけ当てはまる。
    for i in range(n):
        a_i = a_list[i]

        if i != a_i:
            continue
        ans += 1
    
    ans = ans * (ans - 1) // 2

    # i = a_j, j = a_i
    for i, j in enumerate(a_list):
        if i < j and a_list[j] == i:
            ans += 1
            
    print(ans)


if __name__ == "__main__":
    main()
