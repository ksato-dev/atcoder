# -*- coding: utf-8 -*-

if __name__ == "__main__":
    h, w = [int(v) for v in input().split()]
    r, c = [int(v) for v in input().split()]

    ans = 0
    if 1 < r:
        ans += 1
    if r < h:
        ans += 1
    if 1 < c:
        ans += 1
    if c < w:
        ans += 1

    print(ans)
