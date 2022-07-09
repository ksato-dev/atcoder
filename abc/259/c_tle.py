# -*- coding: utf-8 -*-

s = input()
t = input()

n_s = len(s)
n_t = len(t)

if n_s > n_t:
    print("No")
    exit()

# 連続した文字を潰して一致するかどうか見る。
compressed_s = s[0]
compressed_s_cnt = [[s[0], 1]]
cnt = 1
comp_s_cnt_append = compressed_s_cnt.append
for i in range(1, n_s):
    if s[i] == s[i - 1]:
        compressed_s_cnt[-1][1] += 1
    else:
        comp_s_cnt_append([s[i], 1])
        compressed_s += s[i]

compressed_t = t[0]
compressed_t_cnt = [[t[0], 1]]
cnt = 1
comp_t_cnt_append = compressed_t_cnt.append
for i in range(1, n_t):
    if t[i] == t[i - 1]:
        compressed_t_cnt[-1][1] += 1
    else:
        comp_t_cnt_append([t[i], 1])
        compressed_t += t[i]

ans = "No"
if compressed_s == compressed_t:
    ans = "Yes"
    # for s_cnt, t_cnt in zip(compressed_s_cnt, compressed_t_cnt):
    for i in range(len(compressed_s)):
        s_cnt = compressed_s_cnt[i]
        t_cnt = compressed_t_cnt[i]

        cond1 = s_cnt[0] == t_cnt[0]
        cond2 = s_cnt[1] == t_cnt[1]
        cond3 = s_cnt[1] >= 2
        cond4 = s_cnt[1] < t_cnt[1]

        flag = False
        if cond1:
            if cond2 or (cond3 and cond4):
                flag = True
        if not flag:
            ans = "No"
            break

print(ans)
