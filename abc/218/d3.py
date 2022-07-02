
import bisect

if __name__ == "__main__":
    n = int(input())
    point_list = list()

    for i in range(n):
        x, y = [int(v) for v in input().split()]
        point_list.append((x, y))

    point_list.sort()

    cnt = 0
    # p1 が左上に来るケースを考える。
    for i in range(n):
        p1 = point_list[i]
        for j in range(n):
            if i == j:
                continue
            p2 = point_list[j]

            p1_is_in_top_left = p1[0] < p2[0] and p1[1] < p2[1]
            if not p1_is_in_top_left:
                continue

            # 二点決まったので残りの二点も自動的に決まる。
            p3 = (p1[0], p2[1])  # 左下
            p4 = (p2[0], p1[1])  # 右上

            lo = i
            hi = j
            if i > j:
                lo = j
                hi = i

            p3_index = bisect.bisect_left(point_list, (p3), lo=lo, hi=hi)
            # p3_index += 1

            p4_index = bisect.bisect_left(point_list, (p4), lo=lo, hi=hi)
            # p4_index += 1

            try:
                if point_list[p3_index] == p3 and \
                        point_list[p4_index] == p4:
                    cnt += 1
            except:
                continue

    print(cnt)
