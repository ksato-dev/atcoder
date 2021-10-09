if __name__ == "__main__":
    n, p = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]

    cnt = 0
    for a in a_list:
        if a < p:
            cnt += 1

    print(cnt)
