if __name__ == "__main__":
    n = int(input())
    s_list = [int(v) for v in input().split()]
    s_correct_list = [False] * len(s_list)
    
    for b in range(1, 1000):
        for s_id, s in enumerate(s_list):
            a = (s-3 * b) / (4 * b + 3)
            if a > 0 and a.is_integer():
                s_correct_list[s_id] = True

    num_of_non_corrects = n - sum(s_correct_list)
    print(num_of_non_corrects)
