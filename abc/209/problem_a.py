if __name__ == "__main__":
    a, b = [int(v) for v in input().split()]
    ans = b - a + 1

    if ans >= 0:
        print(ans)
    else:
        print(0)
