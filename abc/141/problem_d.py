import heapq

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) * (-1) for v in input().split()]

    heapq.heapify(a_list)
    # 最大値に対してチケットを使い続ける
    for _ in range(m):
        max_a = heapq.heappop(a_list) * (-1)
        heapq.heappush(a_list, int(max_a / 2) * (-1))

    print(sum(a_list) * (-1))
