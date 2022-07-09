# -*- coding: utf-8 -*-

n, m = [int(v) for v in input().split()]
py_list = [None] * m
py_dict = dict()

p_set = set()
for i in range(m):
    p, y = [int(v) for v in input().split()]
    py_list[i] = (p, y)

    if p not in py_dict:
        py_dict[p] = dict()
    if y not in py_dict[p]:
        py_dict[p][y] = None

    p_set.add(p)

# corrdinate compression
for p in p_set:
    y_list = list(py_dict[p].keys())
    y_list.sort()
    py_dict[p] = {y: i + 1 for i, y in enumerate(y_list)}

for p, y in py_list:
    city_id = py_dict[p][y]
    ans_id = str(p).zfill(6) + str(city_id).zfill(6)
    print(ans_id)
