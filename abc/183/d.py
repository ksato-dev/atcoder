n, w = [int(v) for v in input().split()]

# imos method
imos_table = [0] * (2 * 10**5 + 10)
for i in range(n):
    s, t, p = [int(v) for v in input().split()]
    imos_table[s] += p
    imos_table[t] -= p

sum_imos = 0
max_imos = -1
for imos in imos_table:
    sum_imos += imos
    if max_imos < sum_imos:
        max_imos = sum_imos

if max_imos <= w:
    print("Yes")
else:
    print("No")
