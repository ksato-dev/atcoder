if __name__ == "__main__":
    n, sum_money = [int(v) for v in input().split()]

    for x in range(n + 1):
        for y in range(n + 1):
            z = n - (x + y)
            if (z < 0):
                continue

            curr_sum = 10000 * x + 5000 * y + 1000 * z
            if (curr_sum == sum_money):
                print(x, y, z)
                exit()

    print("-1 -1 -1")
