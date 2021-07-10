if __name__ == "__main__":
    n = int(input())
    a_list = [int(a) for a in input().split()]
    a_list.sort()
    count_a_list = [0] * 200000

    max_count = 1

    for a in a_list:
        count_a_list[a] += 1

    a_set = set(a_list)
    for a in a_set:
        curr_count = count_a_list[a]
        curr_count += count_a_list[a + 1]
        if a != 0:
            curr_count += count_a_list[a - 1]

        if max_count < curr_count:
            max_count = curr_count

    print(max_count)
