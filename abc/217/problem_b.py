if __name__ == "__main__":
    contest_list = ["ABC", "ARC", "AGC", "AHC"]
    for _ in range(3):
        in_str = input()
        contest_list.remove(in_str)
    print(contest_list[0])
