def main(n, day_info_list):
    people_cnt = 0
    # day_cnt = 0
    day_cnt_list = [0] * (n+1)
    num_of_day_info = len(day_info_list)
    for day_info_id in range(num_of_day_info-1):
        day_cnt = day_info_list[day_info_id+1][0] - day_info_list[day_info_id][0]
        people_cnt += day_info_list[day_info_id][1]
        day_cnt_list[people_cnt] += day_cnt

    ans_str = ""
    for day_info_id in range(1, n+1):
        ans_str += str(day_cnt_list[day_info_id]) + " "
    print(ans_str)


if __name__ == "__main__":
    n = int(input())
    day_info_list = []
    for _ in range(n):
        start_day, period = [int(v) for v in input().split()]
        end_day = start_day + period
        day_info_list.append((start_day, 1))  # ログインした日にカウント +1
        day_info_list.append((end_day, -1))  # ログインしなくなった日に -1
    day_info_list.sort(key=lambda x: x[0])

    main(n, day_info_list)
