class data():
    def __init__(self):
        self.t = 0
        self.x = 0
        self.y = 0

    def read(self):
        self.t, self.x, self.y = [int(v) for v in input().split()]

    def calc_dt_and_dist(self, bf_data):
        delta_t = self.t - bf_data.t
        dist = abs(self.x - bf_data.x) + abs(self.y - bf_data.y)
        return delta_t, dist


if __name__ == "__main__":
    n = int(input())

    able_plan = True
    bf_data = data()
    for _ in range(n):
        curr_data = data()
        curr_data.read()

        dt, dist = curr_data.calc_dt_and_dist(bf_data)

        if dist > dt:
            able_plan = False
            break
        else:
            eq_even = (dist % 2) == (dt % 2)
            eq_odd = (not dist % 2) == (not dt % 2)

            if eq_even or eq_odd:
                pass
            else:
                able_plan = False
        bf_data = curr_data

    if able_plan:
        print("Yes")
    else:
        print("No")
