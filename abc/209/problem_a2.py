# -*- coding: utf-8 -*-
a, b = [int(v) for v in input().split()]
if b >= a:
    print(b-a+1)
else:
    print(0)
