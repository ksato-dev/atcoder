# -*- coding: utf-8 -*-


k = int(input())

hh = int(k / 60) + 21
mm = k % 60

ans = str(hh).zfill(2) + ":" + str(mm).zfill(2)
print(ans)
