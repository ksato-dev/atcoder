# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a, b, c = [int(v) for v in input().split()]

    ans = 21 - (a + b + c)
    print(ans)
