import numpy as np
import itertools
from numba import njit


class Inputs(object):
    n = 0
    abc_list = []
    # comb_abc = itertools.combinations(list(range(3)), 2)
    perm_abc = list(itertools.permutations(list(range(3)), 2))


def main(inputs):

    # inf = 10 ** 18
    # dp = [[-inf] * 3 for _ in range(inputs.n + 1000)]
    dp = np.full((inputs.n + 1000, 3), 0, dtype=np.int64)
    # dp = np.array(dp, dtype=np.int64)
    dp[0][:] = 0
    # dp[i] := i 日目までで得られる幸福度の最大値dp[ i + 1 ][ j ] := i 日目までの活動履歴のうち、
    # 最終日である i 日目には活動 j (0: A, 1: B, 2: C) を選んだ場合の、得られる幸福度の最大値
    # dp[ i ][ 0 ] から dp[ i + 1 ][ 1 ] への遷移
    # dp[ i ][ 0 ] から dp[ i + 1 ][ 2 ] への遷移
    # dp[ i ][ 1 ] から dp[ i + 1 ][ 0 ] への遷移
    # dp[ i ][ 1 ] から dp[ i + 1 ][ 2 ] への遷移
    # dp[ i ][ 2 ] から dp[ i + 1 ][ 0 ] への遷移
    # dp[ i ][ 2 ] から dp[ i + 1 ][ 1 ] への遷移

    for i in range(inputs.n):
        for perm in inputs.perm_abc:
            src_id = perm[0]
            tgt_id = perm[1]
            cand_dp = dp[i][src_id] + inputs.abc_list[i][tgt_id]
            dp[i+1][tgt_id] = max(dp[i+1][tgt_id], cand_dp)

    print(max(dp[inputs.n]))


if __name__ == "__main__":
    inputs = Inputs()
    inputs.n = int(input())
    for _ in range(inputs.n):
        a, b, c = [int(v) for v in input().split()]
        inputs.abc_list.append((a, b, c))

    main(inputs)
