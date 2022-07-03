import math


def lcm(a, b):
    y = a*b / math.gcd(a, b)
    return int(y)


a, b, c, d = [int(v) for v in input().split()]

# 割り切れる個数を出す。
a_div_c = a // c
b_div_c = b // c

a_div_d = a // d
b_div_d = b // d

cd_lcm = lcm(c, d)
a_div_cd_lcm = a // cd_lcm
b_div_cd_lcm = b // cd_lcm

c_is_divisible = b_div_c - a_div_c + 1
if a % c != 0:
    c_is_divisible -= 1

d_is_divisible = b_div_d - a_div_d + 1
if a % d != 0:
    d_is_divisible -= 1

cd_lcm_is_divisible = b_div_cd_lcm - a_div_cd_lcm + 1
if a % cd_lcm != 0:
    cd_lcm_is_divisible -= 1

# c, d の最小公倍数の割り切れる数を引くと c, d の重複要素がなくなる。
total_divisible_num = c_is_divisible + d_is_divisible - cd_lcm_is_divisible
# print(c_is_divisible, d_is_divisible, cd_lcm_is_divisible)

all_num = b - a + 1
not_divisible_num = all_num - total_divisible_num

print(not_divisible_num)
