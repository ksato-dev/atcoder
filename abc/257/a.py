# -*- coding: utf-8 -*-


n, x = [int(v) for v in input().split()]
str_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

processed_str = ""
for c in str_list:
    processed_str += c * n

print(processed_str[x-1])
