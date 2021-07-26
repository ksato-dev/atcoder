if __name__ == "__main__":
    n = int(input())
    a_list = [int(v) for v in input().split()]
    b_list = [int(v) for v in input().split()]

    xor_lists = []
    for a in a_list:
        curr_xor_list = []
        for b in b_list:
            curr_xor_list.append(a ^ b)
        xor_lists.append(curr_xor_list)

    xor_sets = set()
    for xor_id, curr_xor_list in enumerate(xor_lists):
        curr_xor_set = set(curr_xor_list)
        if xor_id == 0:
            xor_sets = curr_xor_set
        else:
            xor_sets = xor_sets & curr_xor_set

    num_xors = len(xor_sets)
    print(num_xors)
    if num_xors:
        xor_list = list(xor_sets)
        xor_list.sort()
        for xor in xor_list:
            print(xor)
