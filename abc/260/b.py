# -*- coding: utf-8 -*-

n, x, y, z = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]
b_list = [int(v) for v in input().split()]

raw_abi_list = list(zip(a_list, b_list, range(1, n+1), range(n)))

ans_list = list()

# 1 ---
# print("abi_list", raw_abi_list)
abi_list = sorted(raw_abi_list)
# print("abi_list", abi_list)

n1 = n
passed_list = abi_list[n1 - x:]
# print(passed_list)
passed_dict = dict()
# for a, b, i in passed_list1:
for a, b, i, arr_id in abi_list:
    if a not in passed_dict:
        passed_dict[a] = list()
    passed_dict[a].append((i, arr_id))

for a in passed_dict:
    passed_dict[a].sort()

cnt = 0
unique_values = list(set([a for a, _, _, _ in abi_list]))
unique_values.sort()

pop_id_list = list()
for a in reversed(unique_values):
    if cnt >= x:
        break
    for id, arr_id in passed_dict[a]:
        cnt += 1
        ans_list.append(id)
        # print(id)
        # raw_abi_list.pop(arr_id)
        pop_id_list.append(arr_id)
        if cnt >= x:
            break

pop_id_list.sort()
for arr_id in reversed(pop_id_list):
    raw_abi_list.pop(arr_id)
# print("raw:", raw_abi_list)
# --- 1

# 2 ---
# raw_abi_list = [(a, b, id, arr_id) for arr_id, a, b, id, _ in enumerate(raw_abi_list)]
# raw_abi_list = [(a, b, id, arr_id) for arr_id, (a, b, id, _) in enumerate(raw_abi_list)]
raw_abi_list = [(val[0], val[1], val[2], arr_id) for arr_id, val in enumerate(raw_abi_list)]
# raw_abi_list = [a for a in enumerate(raw_abi_list)]
abi_list = sorted(raw_abi_list, key=lambda x: x[1])
# print("abi_list", abi_list)

n2 = n1 - x
passed_list = abi_list[n2 - y:]
# print(passed_list)
passed_dict = dict()
# for a, b, i in passed_list1:
for a, b, i, arr_id in abi_list:
    if b not in passed_dict:
        passed_dict[b] = list()
    passed_dict[b].append((i, arr_id))

for b in passed_dict:
    passed_dict[b].sort()

cnt = 0
unique_values = list(set([b for _, b, _, _ in abi_list]))
unique_values.sort()

pop_id_list = list()
for b in reversed(unique_values):
    if cnt >= y:
        break
    for id, arr_id in passed_dict[b]:
        cnt += 1
        ans_list.append(id)
        # print(id)
        # raw_abi_list.pop(arr_id)
        pop_id_list.append(arr_id)
        if cnt >= y:
            break

pop_id_list.sort()
for arr_id in reversed(pop_id_list):
    raw_abi_list.pop(arr_id)
# print("raw:", raw_abi_list)
# --- 2

# 3 ---
raw_ci_list = [(val[0] + val[1], val[2], arr_id) for arr_id, val in enumerate(raw_abi_list)]
ci_list = sorted(raw_ci_list)
# print("ci_list", ci_list)

n3 = n2 - y
passed_list = ci_list[n3 - z:]
# print(passed_list)
passed_dict = dict()
# for a, b, i in passed_list1:
for c, i, arr_id in ci_list:
    if c not in passed_dict:
        passed_dict[c] = list()
    passed_dict[c].append((i, arr_id))

for c in passed_dict:
    passed_dict[c].sort()

cnt = 0
unique_values = list(set([c for c, _, _ in ci_list]))
unique_values.sort()

pop_id_list = list()
for c in reversed(unique_values):
    if cnt >= z:
        break
    for id, arr_id in passed_dict[c]:
        cnt += 1
        ans_list.append(id)
        # print(id)
        # raw_ci_list.pop(arr_id)
        pop_id_list.append(arr_id)
        if cnt >= z:
            break

pop_id_list.sort()
for arr_id in reversed(pop_id_list):
    raw_ci_list.pop(arr_id)

# print("raw:", raw_ci_list)

for ans in sorted(ans_list):
    print(ans)
# --- 3
