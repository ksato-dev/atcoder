
import heapq

q = int(input())

heap_data = list()
heapq.heapify(heap_data)

offset = 0
for i in range(q):
    query = [int(v) for v in input().split()]
    q_id = query[0]
    if (q_id == 1):
        x = query[1]
        heapq.heappush(heap_data, x - offset)
    elif (q_id == 2):
        x = query[1]
        offset += x
        # heapq.heappush(heap_data, x)
    elif (q_id == 3):
        ans = heapq.heappop(heap_data) + offset
        print(ans)
