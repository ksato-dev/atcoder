if __name__ == "__main__":
    x_list = [int(c) for c in input()]

    is_weak = False

    if x_list[0] == x_list[1] == x_list[2] == x_list[3]:
        is_weak = True
        print("Weak")
        exit()

    is_continue = True
    for x_id in range(0, len(x_list) - 1):
        if x_list[x_id] != 9:
            if x_list[x_id] + 1 != x_list[x_id + 1]:
                is_continue = False
        else:
            if x_list[x_id + 1] != 0:
                is_continue = False

    if is_continue:
        is_weak = True

    if is_weak:
        print("Weak")
    else:
        print("Strong")
