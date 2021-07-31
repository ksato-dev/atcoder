import heapq

if __name__ == "__main__":
    q_num = int(input())
    q_list = [input().split() for _ in range(q_num)]
    p_list = []

    ope3_p_list = []
    sum_ope2 = 0
    for q in q_list:
        ope = q[0]
        if ope == "1":
            x = int(q[1])
            heapq.heappush(p_list, x - sum_ope2)
        elif ope == "2":
            x = int(q[1])
            sum_ope2 = sum_ope2 + x
        elif ope == "3":
            ope3_p_list.append(heapq.heappop(p_list) + sum_ope2)

    for p in ope3_p_list:
        print(p)
