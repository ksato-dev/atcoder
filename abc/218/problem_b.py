import string

if __name__ == "__main__":
    p_list = [int(v) for v in input().split()]
    ascii_str_list = list(string.ascii_lowercase)

    ans_str = ""
    for p in p_list:
        ans_str += ascii_str_list[p-1]
    print(ans_str)
