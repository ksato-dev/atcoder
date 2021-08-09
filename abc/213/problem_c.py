def main():
    h, w, n = [int(v) for v in input().split()]

    a_list = []
    b_list = []
    for n_id in range(n):
        a, b = [int(v) - 1 for v in input().split()]
        a_list.append(a)
        b_list.append(b)

    set_a = set(a_list)
    set_b = set(b_list)
    sorted_set_a = sorted(list(set_a))
    sorted_set_b = sorted(list(set_b))

    # ID の変換テーブルを作る
    a_dict = {a: cnt+1 for cnt, a in enumerate(sorted_set_a)}
    b_dict = {b: cnt+1 for cnt, b in enumerate(sorted_set_b)}

    for i in range(n):
        a = a_dict[a_list[i]]
        b = b_dict[b_list[i]]
        print(a, b)
    

if __name__ == "__main__":
    main()
