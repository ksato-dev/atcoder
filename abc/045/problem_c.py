def recursive_sum(s, i, partial_s):
    size_s = len(s)
    if size_s - i == 1:
        return sum(map(int, partial_s.split("+")))

    val1 = recursive_sum(s, i + 1, partial_s + s[i + 1])
    val2 = recursive_sum(s, i + 1, partial_s + "+" + s[i + 1])
    return val1 + val2


if __name__ == "__main__":
    s = input()
    result = recursive_sum(s, 0, s[0])
    print(result)
