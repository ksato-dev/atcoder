import heapq

if __name__ == "__main__":
    n, k = [int(v) for v in input().split()]
    a_list = [int(v) * -1 for v in input().split()]
    heapq.heapify(a_list)

    sum_satisfaction = 0
    for k_id in range(k):
        a_max = heapq.heappop(a_list) * -1

        if a_max == 0:
            break

        sum_satisfaction = sum_satisfaction + a_max
        heapq.heappush(a_list, (a_max - 1) * - 1)

    print(sum_satisfaction)
