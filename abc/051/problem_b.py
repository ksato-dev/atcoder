if __name__ == "__main__":
    k, s = [int(v) for v in input().split()]

    cnt = 0
    for x in range(k + 1):
        for y in range(k + 1):
            z = s - x - y
            if 0 <= z <= k:
                cnt = cnt + 1

    print(cnt)
