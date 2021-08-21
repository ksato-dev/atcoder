from itertools import permutations


def main():
    s, k = [v for v in input().split()]
    k = int(k)
    # print(s, k)
    str_list = list(permutations(s))
    str_set = set(str_list)
    # print(str_set)
    str_list = sorted(list(str_set))
    ans = "".join(str_list[k - 1])
    print(ans)


if __name__ == "__main__":
    main()
