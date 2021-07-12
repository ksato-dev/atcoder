import math


def calc_distance(p1, p2):
    diff_p1_squared = (p1[0] - p2[0]) ** 2
    diff_p2_squared = (p1[1] - p2[1]) ** 2
    dist = math.sqrt(diff_p1_squared + diff_p2_squared)
    return dist


if __name__ == "__main__":
    n = int(input())
    xy_list = []
    for _ in range(n):
        x, y = [float(v) for v in input().split()]
        xy_list.append((x, y))

    max_dist = -1
    for i in range(0, n):
        for j in range(i + 1, n):
            p1 = xy_list[i]
            p2 = xy_list[j]
            dist = calc_distance(p1, p2)
            if max_dist < dist:
                max_dist = dist

    print(round(max_dist, 6))
