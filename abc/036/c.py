
n = int(input())
a_list = []

for i in range(n):
    a_list.append(int(input()))

# b_list = copy.deepcopy(a_list)
b_set = sorted(set(a_list))
b_dict = {b: i for i, b in enumerate(b_set)}

b_list = [b_dict[a] for a in a_list]

for b in b_list:
    print(b)
