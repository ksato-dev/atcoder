def read_c_ij_matrix():
    first_row_str = input()
    first_row_int = map(int, first_row_str.split())

    ret_c_ij_matrix = []
    ret_c_ij_matrix.append(list(first_row_int))
    num_dim = len(ret_c_ij_matrix[0])

    for row_id in range(1, num_dim):
        curr_row_str = input()
        curr_row_int = map(int, curr_row_str.split())
        ret_c_ij_matrix.append(list(curr_row_int))

    return ret_c_ij_matrix


def get_b_j_list(a1, c_ij_matrix):
    ret_b_j_list = []
    num_dim = len(c_ij_matrix[0])

    for j in range(0, num_dim):
        b_j = c_ij_matrix[0][j] - a1
        if check_minus(b_j):
            ret_b_j_list = []
            break
        ret_b_j_list.append(b_j)

    return ret_b_j_list


def get_a_i(i, b_j_list, c_ij_matrix):
    num_dim = len(b_j_list)

    a_candidates = []
    for j in range(0, num_dim):
        b_j = b_j_list[j]
        a = c_ij_matrix[i-1][j] - b_j
        a_candidates.append(a)

    for a in a_candidates:
        if a != a_candidates[0]:
            return -1

    if check_minus(a_candidates[0]):
        return -1

    ret_a = a_candidates[0]

    return ret_a


def check_minus(value):
    return (value < 0)


def main():
    c_ij_matrix = read_c_ij_matrix()

    min_a1 = 0
    max_a1 = 100

    adopted_a_i_list = None
    adopted_b_j_list = None

    for a1 in range(min_a1, max_a1 + 1):
        b_j_list = get_b_j_list(a1, c_ij_matrix)
        if b_j_list is not None:
            # print(a1, b_j_list)
            num_dim = len(b_j_list)
            a_i_list = [a1]

            for i in range(2, num_dim+1):  # +1 しないと最後が処理されない
                a_i = get_a_i(i, b_j_list, c_ij_matrix)
                if check_minus(a_i):
                    a_i = None

                a_i_list.append(a_i)
            if None in a_i_list:
                continue
            else:
                adopted_a_i_list = a_i_list
                adopted_b_j_list = b_j_list
                break

    is_none = None in adopted_a_i_list or None in adopted_b_j_list
    is_blank = not adopted_a_i_list or not adopted_b_j_list
    if is_none or is_blank:
        print("No")
    else:
        # print(adopted_a_i_list, adopted_b_j_list)
        print("Yes")


if __name__ == "__main__":
    main()
