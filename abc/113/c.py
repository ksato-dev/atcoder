n, m = [int(v) for v in input().split()]

py_dict = {i + 1: list() for i in range(n)}
p_list = list()
y_list = list()
for i in range(m):
    p, y = [int(v) for v in input().split()]
    p_list.append(p)
    y_list.append(y)
    py_dict[p].append(y)

ans_dict = dict()
for p in py_dict:
    sorted_y_list = sorted(py_dict[p])
    city_id_dict = {y: str(p).zfill(6) + str(i + 1).zfill(6)
                    for i, y in enumerate(sorted_y_list)}
    ans_dict[p] = city_id_dict

for p, y in zip(p_list, y_list):
    city_id = ans_dict[p][y]
    print(city_id)
