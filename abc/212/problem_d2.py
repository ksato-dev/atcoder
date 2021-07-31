import heapq

if __name__ == "__main__":
    q_num = int(input())
    x_list = []

    heapq.heapify(x_list)

    cum_sum = 0
    for q_id in range(q_num):
        query = [int(v) for v in input().split()]
        q_type = query[0]

        ope3_x_list = []
        if q_type == 1:
            x = query[1]
            heapq.heappush(x_list, x - cum_sum)
        elif q_type == 2:
            x = query[1]
            cum_sum = cum_sum + x
        elif q_type == 3:
            x = heapq.heappop(x_list)
            ope3_x_list.append(x + cum_sum)

        for x in ope3_x_list:
            print(x)
