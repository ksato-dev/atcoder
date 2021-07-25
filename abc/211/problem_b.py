if __name__ == "__main__":
    str_list = [input() for _ in range(4)]
    str_set = set(str_list)

    if len(str_set) == 4:
        print("Yes")
    else:
        print("No")
