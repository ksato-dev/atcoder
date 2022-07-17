# -*- coding: utf-8 -*-

s = input()
s_dict = dict()

for c in s:
    if c not in s_dict:
        s_dict[c] = 1
    else:
        s_dict[c] += 1

for key, val in s_dict.items():
    if val == 1:
        print(key)
        exit()

print(-1)
