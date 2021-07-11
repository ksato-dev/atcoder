class data(object):
    def __init__(self, x=-1, y=-1, h=-1):
        self.x = x
        self.y = y
        self.h = h

    def __repr__(self):
        return repr((self.x, self.y, self.h))


if __name__ == "__main__":
    n = int(input())
    data_list = []
    for _ in range(n):
        x, y, h = [int(v) for v in input().split()]
        data_list.append(data(x, y, h))

    data_list.sort(key=lambda x: x.h, reverse=True)

    max_xy = 100
    for cx in range(max_xy + 1):
        for cy in range(max_xy + 1):
            h_top0 = 0
            for arr_id, d in enumerate(data_list):
                diff_x = abs(d.x - cx)
                diff_y = abs(d.y - cy)
                h_top = d.h + diff_x + diff_y

                # 高さが０のときのデータは使用しない
                # 高さが０のデータが存在する＝グリッド境界上に頂点がある
                if d.h == 0:
                    continue

                h_top0 = h_top

            is_corrent_h = True
            for arr_id, d in enumerate(data_list):
                diff_x = abs(d.x - cx)
                diff_y = abs(d.y - cy)
                h = max(h_top0 - diff_x - diff_y, 0)

                if d.h != h:
                    is_corrent_h = False
                    break

            if is_corrent_h and h_top0 is not None:
                print(cx, cy, h_top0)
                exit()
