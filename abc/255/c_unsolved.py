# -*- coding: utf-8 -*-
import bisect


if __name__ == "__main__":
    # 入力が大きくなると無理
    x, a, d, n = [int(v) for v in input().split()]
    s = [a + d * i for i in range(n)]

    s.sort()
    print(s)
    print(len(s))
    close_id = bisect.bisect(s, x) - 1
    print(close_id)
    value = s[close_id]

    if x < value:
        diff = value - x
        if close_id > 0:
            value2 = s[close_id-1]
            diff2 = x - value2

            if diff > diff2:
                diff = diff2
    else:
        diff = x - value
        if len(s) - 1 > close_id:
            value2 = s[close_id+1]
            diff2 = value2 - x

            if diff > diff2:
                diff = diff2

        print(diff)




