def read_a_list():
    line = input()
    arr_str = line.split()
    ret_data = list(map(int, arr_str))

    return ret_data


def read_data():
    line = input()
    ret_data = int(line)

    return ret_data


if __name__ == "__main__":
    N, C, K = read_a_list()
    time_list = [read_data() for _ in range(N)]

    sorted_time_list = sorted(time_list)

    bus_list = []
    curr_bus = []
    for arrived_time in sorted_time_list:
        if len(curr_bus) == 0:
            curr_bus.append(arrived_time)
        else:
            flag1 = len(curr_bus) < C
            flag2 = arrived_time - curr_bus[0] <= K
            if flag1 and flag2:
                curr_bus.append(arrived_time)
            else:
                if len(curr_bus) != 0:
                    bus_list.append(curr_bus)
                    curr_bus = []

                curr_bus.append(arrived_time)

    # 上記の処理だけだと、一番最後に来たバスが bus_list に追加されない場合があるので
    # ループ出た後に curr_bus 内に要素があるなら bus_list に apeend する。
    if len(curr_bus) > 0:
        bus_list.append(curr_bus)

    print(len(bus_list))
