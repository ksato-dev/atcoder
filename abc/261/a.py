# -*- coding: utf-8 -*-


def main():
    l1, r1, l2, r2 = [int(v) for v in input().split()]

    data = [0] * 110

    for i in range(l1, r1):
        data[i] += 1

    for i in range(l2, r2):
        data[i] += 1

    print(data.count(2))


if __name__ == "__main__":
    main()
