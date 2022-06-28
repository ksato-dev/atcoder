n = int(input())
l_list = [int(v) for v in input().split()]
l_list.sort()

ans = 0
for i in range(n-2):
    a = l_list[i]
    for j in range(i + 1, n-1):
        b = l_list[j]
        for k in range(j + 1, n):
            c = l_list[k]

            cond1 = a < (b + c)
            cond2 = b < (c + a)
            cond3 = c < (a + b)
            if cond1 and cond2 and cond3:
                ans += 1

print(ans)
