import bisect

n = int(input())
l_list = [int(v) for v in input().split()]
l_list.sort()

ans = 0
for i in range(n-2):
    a = l_list[i]
    for j in range(i + 1, n-1):
        b = l_list[j]
        c_upper_bound = a + b
        upper_bound_id = bisect.bisect_left(l_list, c_upper_bound)
        ans += (upper_bound_id - 1) - j

print(ans)
