h, w, n = [int(v) for v in input().split()]
a_list = [None] * n
b_list = [None] * n

for i in range(n):
    a, b = [int(v) for v in input().split()]
    a_list[i] = a
    b_list[i] = b

sorted_a_set = sorted(set(a_list))
sorted_b_set = sorted(set(b_list))
a_zaatsu_dict = {v: i for i, v in enumerate(sorted_a_set)}
b_zaatsu_dict = {v: i for i, v in enumerate(sorted_b_set)}

# zaatsued_h = len(sorted_a_set)
# zaatsued_w = len(sorted_b_set)

# ans_mat = [["*"] * zaatsued_w for _ in range(zaatsued_h)]
for i in range(n):
    a = a_list[i]
    b = b_list[i]
    zaatsued_a_id = a_zaatsu_dict[a]
    zaatsued_b_id = b_zaatsu_dict[b]
    # ans_mat[zaatsued_a_id][zaatsued_b_id] = str(i + 1)
    print(zaatsued_a_id + 1, zaatsued_b_id + 1)

# for i in range(zaatsued_h):
#     for j in range(zaatsued_w):
#         print(ans_mat[i][j], end="")
#     print()
