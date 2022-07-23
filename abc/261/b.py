# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a_map = [None] * n
    for i in range(n):
        a_map[i] = input()
    
    # print(a_map)

    correct = True
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elem1 = a_map[i][j]
            elem2 = a_map[j][i]

            flag1 = elem1 == "W" and elem2 == "L"
            flag2 = elem1 == "L" and elem2 == "W"
            flag3 = elem1 == "D" and elem2 == "D"

            if flag1 or flag2 or flag3:
                pass
            else:
                correct = False
                break

    if correct:
        print("correct")
    else:
        print("incorrect")



if __name__ == "__main__":
    main()
