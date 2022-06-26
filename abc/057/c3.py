# -*- coding :utf-8 -*-

import math

n = int(input())

# a = b の時、a = b = sqrt(n), a を小さくすると、b は大きくなるので
# a <= b になり、a の上限は sqrt(n) と言って良いため、この性質を利用する。

min_digit = 10 ** 10
for a in range(1, int(math.sqrt(n)) + 1):
    if n % a == 0:
        b = n // a
        digit1 = len(str(a))
        digit2 = len(str(b))
        tmp = max(digit1, digit2)
        if tmp < min_digit:
            min_digit = tmp

print(min_digit)
