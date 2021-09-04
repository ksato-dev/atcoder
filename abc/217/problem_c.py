if __name__ == "__main__":
    n = int(input())
    p_list = [int(v) for v in input().split()]
    q_list = [0] * n
    for q_val, p in enumerate(p_list):
        q_list[p - 1] = q_val + 1

    ans_q_list = list(map(str, q_list))
    print(" ".join(ans_q_list))
