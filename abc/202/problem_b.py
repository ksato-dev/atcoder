# -*- coding: utf-8 -*-

if __name__ == "__main__":
    in_str = input()

    ans_str = ""
    for s in reversed(in_str):
        add_c = s
        if s == "6":
            add_c = "9"
        elif s == "9":
            add_c = "6"
        ans_str += add_c
    print(ans_str)
