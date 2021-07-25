def get_matched_ids(string, c):
    ret_matched_ids = []
    c_id = 0
    for c_id, char in enumerate(string):
        if char == c:
            ret_matched_ids.append(c_id)

    return ret_matched_ids


if __name__ == "__main__":
    string = input()

    name = "chokudai"
    ids_dict = dict()
    ids_dict["c"] = get_matched_ids(string, "c")
    ids_dict["h"] = get_matched_ids(string, "h")
    ids_dict["o"] = get_matched_ids(string, "o")
    ids_dict["k"] = get_matched_ids(string, "k")
    ids_dict["u"] = get_matched_ids(string, "u")
    ids_dict["d"] = get_matched_ids(string, "d")
    ids_dict["a"] = get_matched_ids(string, "a")
    ids_dict["i"] = get_matched_ids(string, "i")

    cnt = 0
    for c_id in ids_dict["c"]:
        for h_id in ids_dict["h"]:
            if c_id >= h_id:
                continue
            for o_id in ids_dict["o"]:
                if h_id >= o_id:
                    continue
                for k_id in ids_dict["k"]:
                    if o_id >= k_id:
                        continue
                    for u_id in ids_dict["u"]:
                        if k_id >= u_id:
                            continue
                        for d_id in ids_dict["d"]:
                            if u_id >= d_id:
                                continue
                            for a_id in ids_dict["a"]:
                                if d_id >= a_id:
                                    continue
                                for i_id in ids_dict["i"]:
                                    if a_id >= i_id:
                                        continue
                                    cnt = cnt + 1

    print(cnt % (10**9 + 7))
