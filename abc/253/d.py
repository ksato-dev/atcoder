import math

# Comment: 最小公倍数に気づくのに時間かかりすぎ。


def lcm(a, b):
    # 2数を受け取って最小公倍数を返す関数
    y = a*b / math.gcd(a, b)
    return int(y)


n, a, b = [int(v) for v in input().split()]
all_sum = n * (n + 1) // 2

num_a = n // a
num_b = n // b
gcd = lcm(a, b)
num_gcd = n // gcd

# 等差数列の和
a_sum = num_a * (2 * a + (num_a - 1) * a) // 2
b_sum = num_b * (2 * b + (num_b - 1) * b) // 2
gcd_sum = num_gcd * (2 * gcd + (num_gcd - 1) * gcd) // 2

print(all_sum - (a_sum + b_sum - gcd_sum))
