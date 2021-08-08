if __name__ == "__main__":
    n = int(input())
    a_list = [int(c) for c in input().split()]
    a_dict = dict()
    for a_id in range(n):
        a_dict[a_id + 1] = a_list[a_id]

    a_sorted = sorted(a_dict.items(), key=lambda x:x[1])

    print(a_sorted[-2][0])