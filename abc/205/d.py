import bisect

n, q = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]

c_list = [a - (i + 1) for i, a in enumerate(a_list)]

for i in range(q):
    k = int(input())
    if c_list[-1] < k:
        print(a_list[-1] + (k - c_list[-1]))
    else:
        c_id = bisect.bisect_left(c_list, k)
        c = c_list[c_id]
        # print("c info:", c_list[c_id - 1], c_list[c_id])
        print((a_list[c_id] - 1) - (c - k))
