# -*- coding: utf-8 -*-


n, m, x, t, d = [int(v) for v in input().split()]

ans = t
if m > x:
    pass
else:
    if m > x:
        ans -= (m - x) * d
    else:
        ans -= (x - m) * d

print(ans)
