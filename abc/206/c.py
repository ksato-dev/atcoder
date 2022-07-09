
n = int(input())
a_list = [int(v) for v in input().split()]

a_info_dict = dict()  # {a: cnt_in_a_list}
for a in a_list:
    if a not in a_info_dict:
        a_info_dict[a] = 0
    a_info_dict[a] += 1

ans = 0
for i in range(n - 1):
    a = a_list[i]  # Ai
    rest_of_a_cnt = a_info_dict[a] - 1
    a_info_dict[a] = rest_of_a_cnt
    ans += (n - (i + 1)) - rest_of_a_cnt  # Aj の数を可算

print(ans)
