if __name__ == "__main__":
    n = int(input())
    fullname_list = []
    for _ in range(n):
        s, t = [v for v in input().split()]
        if (s, t) in fullname_list:
            print("Yes")
            exit()
        fullname_list.append((s, t))

    print("No")
