def read_data():
    ret_data = input()

    return ret_data


if __name__ == "__main__":
    keywords = ["dream", "dreamer", "erase", "eraser"]
    reversed_keywords = [kw[::-1] for kw in keywords]
    s = read_data()

    info_truth = False
    reversed_s = s[::-1]
    reversed_t = ""

    next_c_id = 0
    for c_id, char in enumerate(reversed_s):
        if next_c_id > c_id:
            continue

        for r_kw in reversed_keywords:
            num_of_str = len(r_kw)
            extracted_str = reversed_s[c_id:c_id+num_of_str]

            if r_kw == extracted_str:
                reversed_t += extracted_str
                next_c_id = c_id + num_of_str
                break
        else:
            next_c_id = c_id

    t = reversed_t[::-1]
    # print(t)

    if s == t:
        info_truth = True

    if info_truth:
        print("YES")
    else:
        print("NO")
