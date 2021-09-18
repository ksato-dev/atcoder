import string

if __name__ == "__main__":
    x = input()
    n = int(input())
    str_cost_dict = dict()

    ascii_str_list = list(string.ascii_lowercase)
    for x_id in range(len(x)):
        str_cost_dict[x[x_id]] = ascii_str_list[x_id]

    str_list = list()
    len_max = -1
    for n_id in range(n):
        curr_str = input()
        str_list.append(curr_str)
        if len_max < len(curr_str):
            len_max = len(curr_str)

    cost_and_src_id_list = list()
    for n_id in range(n):
        curr_str = str_list[n_id]
        curr_cost_str = ""
        for c in curr_str:
            curr_cost_str = curr_cost_str + str_cost_dict[c]

        curr_cost_str.ljust(len_max, "0")
        cost_and_src_id = (curr_cost_str, n_id)
        cost_and_src_id_list.append(cost_and_src_id)

    cost_and_src_id_list.sort()

    for elem in cost_and_src_id_list:
        print(str_list[elem[1]])
