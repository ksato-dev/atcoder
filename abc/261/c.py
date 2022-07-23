# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s_dict = dict()
    s = input()
    s_dict[s] = 1
    # print(s)

    ans = list()
    ans.append(s)

    for i in range(1, n):
        s = input()
        if s not in s_dict:
            s_dict[s] = 0
            ans.append(s)
        else:
            ans.append(s + "(" + str(s_dict[s]) + ")")
        s_dict[s] += 1

    for a in ans:
        print(a)
    


if __name__ == "__main__":
    main()
