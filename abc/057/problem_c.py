def read_data():
    line = input()
    ret_data = int(line)

    return ret_data


def F(A, B):
    A_digit = len(str(A))
    B_digit = len(str(B))
    return max(A_digit, B_digit)


# 約数を求める速いアルゴリズム
# https://ictsr4.com/py/m0120.html


def divisors_list_s(num):
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)  # 約数をリストに追加
            if i ** 2 == num:  # 重解の場合に2つリストされるのを防ぐ
                continue
            divisors.append(num // i)  # 約数の相手方をリストに追加
    #     return divisors         #昇順にしなくてよいならソートは不要
    return sorted(divisors)  # 昇順にしたいときはソートする


if __name__ == "__main__":
    N = read_data()

    min_digit = 1e20
    divisors_list = divisors_list_s(N)
    for a in divisors_list:
        remainder = N % a
        if remainder != 0:
            continue
        b = N / a
        digit = F(int(a), int(b))
        min_digit = min(digit, min_digit)

    print(min_digit)
