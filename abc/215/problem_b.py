if __name__ == "__main__":
    n = int(input())
    k = 0
    while True:
        ans = 2 ** k
        if n < ans:
            if 0 < k:
                k -= 1
            break
        k += 1

    print(k)
