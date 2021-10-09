import numpy as np


def judge_janken(a1_id, a1_ope, a2_id, a2_ope):
    res = None
    if a1_ope == "G":
        if a2_ope == "G":
            pass
        elif a2_ope == "C":
            res = a1_id
        elif a2_ope == "P":
            res = a2_id
    elif a1_ope == "C":
        if a2_ope == "G":
            res = a2_id
        elif a2_ope == "C":
            pass
        elif a2_ope == "P":
            res = a1_id
    elif a1_ope == "P":
        if a2_ope == "G":
            res = a1_id
        elif a2_ope == "C":
            res = a2_id
        elif a2_ope == "P":
            pass
    return res


def main(n, m, a_ope_dict):
    a_id_rank_cnt_list = [[v+1, v+1, 0]
                          for v in range(n * 2)]  # [a_id, rank, win_cnt]
    a_id_rank_cnt_list = np.array(a_id_rank_cnt_list)

    if n == 1:
        a1_list = a_ope_dict[1]
        a2_list = a_ope_dict[2]
        a1_cnt = 0
        a2_cnt = 0

        for a1_ope, a2_ope in zip(a1_list, a2_list):
            a1_id = 1
            a2_id = 2
            win_id = judge_janken(a1_id, a1_ope, a2_id, a2_ope)

            if a1_id == win_id:
                a1_cnt += 1
            elif a2_id == win_id:
                a2_cnt += 1
        if a1_cnt >= a2_cnt:
            print(1)
            print(2)
        else:
            print(2)
            print(1)
        exit()

    for m_id in range(m):
        sorted_list_using_cnt = \
            a_id_rank_cnt_list[a_id_rank_cnt_list[:, 2].argsort(), :]
        cnt_set = sorted(list(set(sorted_list_using_cnt[:, 2])), reverse=True)
        offset_rank = 1
        reranked_list = np.array([])
        while offset_rank < n:
            for cnt in cnt_set:
                a_id_list = [[a_id, None, c]
                             for a_id, r, c in sorted_list_using_cnt if c == cnt]
                a_id_list.sort(key=lambda x: x[0])
                for arr_id, _ in enumerate(a_id_list):
                    a_id = a_id_list[arr_id][0]
                    rank = arr_id + offset_rank
                    cnt = a_id_list[arr_id][2]
                    a_id_list[arr_id] = [a_id, rank, cnt]
                reranked_list = np.append(reranked_list, np.array(a_id_list))
                reranked_list = np.reshape(reranked_list, (-1, 3))
                offset_rank += len(a_id_list)

        for arr_id, value in enumerate(reranked_list):
            if arr_id % 2 == 0:
                continue

            a1_id = reranked_list[arr_id - 1][0]
            a2_id = reranked_list[arr_id][0]
            a1_ope = a_ope_dict[a1_id][m_id]
            a2_ope = a_ope_dict[a2_id][m_id]
            win_id = judge_janken(a1_id, a1_ope, a2_id, a2_ope)

            if a1_id == win_id:
                reranked_list[arr_id - 1][2] += 1
            elif a2_id == win_id:
                reranked_list[arr_id][2] += 1

        a_id_rank_cnt_list = reranked_list

        if m_id == m - 1:
            sorted_list_using_cnt = \
                a_id_rank_cnt_list[a_id_rank_cnt_list[:, 2].argsort(), :]
            cnt_set = sorted(
                list(set(sorted_list_using_cnt[:, 2])), reverse=True)
            offset_rank = 1
            reranked_list = np.array([])
            while offset_rank < n:
                for cnt in cnt_set:
                    a_id_list = [[a_id, None, c]
                                 for a_id, r, c in sorted_list_using_cnt if c == cnt]
                    a_id_list.sort(key=lambda x: x[0])
                    for arr_id, _ in enumerate(a_id_list):
                        a_id = a_id_list[arr_id][0]
                        rank = arr_id + offset_rank
                        cnt = a_id_list[arr_id][2]
                        a_id_list[arr_id] = [a_id, rank, cnt]
                    reranked_list = np.append(
                        reranked_list, np.array(a_id_list))
                    reranked_list = np.reshape(reranked_list, (-1, 3))
                    offset_rank += len(a_id_list)
            a_id_rank_cnt_list = reranked_list

    for res in a_id_rank_cnt_list[:, 0]:
        print(int(res))


if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_ope_dict = {}
    for arr_id in range(n * 2):
        a_ope_dict[arr_id + 1] = [v for v in input()]
    main(n, m, a_ope_dict)
