# -*- coding: utf-8 -*-

def main():
    n, x = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]
    for i in range(1, len(a_list), 2):
        a_list[i] = a_list[i] - 1

    if x >= sum(a_list):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
