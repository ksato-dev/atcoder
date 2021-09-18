if __name__ == "__main__":
    str_list = list()
    str_list.append(input())
    str_list.append(input())
    str_list.append(input())
    t = input()

    ans_str = ""
    for t_id in range(len(t)):
        n = int(t[t_id]) - 1
        ans_str += str_list[n]
    print(ans_str)
