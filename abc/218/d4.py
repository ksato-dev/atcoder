
import bisect

n = int(input())
point_list = [None] * n
for i in range(n):
    x, y = [int(v) for v in input().split()]
    point_list[i] = (x, y)
point_list.sort()

bbox_cnt = 0
for i in range(n):
    top_left_point = point_list[i]
    for j in range(n):
        btm_right_point = point_list[j]

        skip_flag_x = top_left_point[0] >= btm_right_point[0]
        skip_flag_y = top_left_point[1] >= btm_right_point[1]
        if skip_flag_x or skip_flag_y:
            continue

        # 2点決まったのでもう２点を決める。
        top_right_point = (btm_right_point[0], top_left_point[1])
        btm_left_point = (top_left_point[0], btm_right_point[1])

        # 自動的に決まった２点が存在するか調べる。
        tr_id = bisect.bisect_left(point_list, top_right_point)
        bl_id = bisect.bisect_left(point_list, btm_left_point)
        
        match_tr = point_list[tr_id] == top_right_point
        match_bl = point_list[bl_id] == btm_left_point

        if match_tr and match_bl:
            bbox_cnt += 1
        
print(bbox_cnt)
