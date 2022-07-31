# -*- coding: utf-8 -*-


def main():
    y = int(input())
    ans = y % 4

    if ans == 2:
        print(y)
    else:
        if ans == 0:
            print(y + 2)
        elif ans == 1:
            print(y + 1)
        elif ans == 3:
            print(y + 3)


if __name__ == "__main__":
    main()
