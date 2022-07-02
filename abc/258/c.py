# -*- coding: utf-8 -*-


n, q = [int(v) for v in input().split()]
s = input()

start_id = 0
for i in range(q):
    t, x = [int(v) for v in input().split()]
    if t == 1:
        start_id -= x
        if start_id < 0:
            start_id = n - abs(start_id)
        elif n <= start_id:
            start_id = start_id - n
    elif t == 2:
        ref_id = start_id + x - 1
        if n <= ref_id:
            ref_id = ref_id - n

        print(s[ref_id])
