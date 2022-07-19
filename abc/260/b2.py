
def pass_students(unique_v_list, student_list, v_id, pass_limit, ans_id_list):
    # 点数別に id のリストを作る。
    v_ids_dict = {v: list() for v in unique_v_list}
    for student in reversed(student_list):
        # a, b, ab, id, passed = student
        v = student[v_id]
        id = student[3]
        passed = student[4]
        if passed is True:
            continue
        v_ids_dict[v].append(id)

    cnt = 0
    # 点数の大きい順から id を調べる
    for v in reversed(unique_v_list):
        if cnt >= pass_limit:
            break
        v_ids_dict[v].sort()  # 若い id から見ていきたいので、ソートする。
        for id in v_ids_dict[v]:
            if cnt >= pass_limit:
                break

            # 今見てる ID と一致する要素を調べ、未合格であれば情報更新＆答えを格納。
            for arr_id, student in enumerate(student_list):
                curr_id = student[3]
                passed = student[4]
                if passed is True:
                    continue
                if curr_id != id:
                    continue

                ans_id_list.append(id)
                student_list[arr_id][4] = True
                cnt += 1
                if cnt >= pass_limit:
                    break


n, x, y, z = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]
b_list = [int(v) for v in input().split()]

# (a, b, ab, id, passed)
ab_list = [a + b for a, b in zip(a_list, b_list)]
student_list = list(zip(a_list, b_list, ab_list, range(1, n + 1), [False] * n))
student_list = [list(tuple_data) for tuple_data in student_list]

ans_id_list = list()

# for a
student_list.sort()
unique_a_list = sorted(list(set(a_list)))
pass_students(unique_a_list, student_list, 0, x, ans_id_list)

# for b
student_list.sort(key=lambda x: x[1])
unique_b_list = sorted(list(set(b_list)))
pass_students(unique_b_list, student_list, 1, y, ans_id_list)

# for ab
student_list.sort(key=lambda x: x[2])
unique_ab_list = sorted(list(set(ab_list)))
pass_students(unique_ab_list, student_list, 2, z, ans_id_list)

ans_id_list.sort()
for ans in ans_id_list:
    print(ans)
