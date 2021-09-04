if __name__ == "__main__":
    str_list = [v for v in input().split()]
    s = str_list[0]
    t = str_list[1]
    copied_str_list = sorted(str_list)

    if s == copied_str_list[0]:
        print("Yes")
    else:
        print("No")
