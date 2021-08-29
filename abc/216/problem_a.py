if __name__ == "__main__":
    x, y = [int(v) for v in input().split(".")]

    postfix = None
    if 0 <= y <= 2:
        postfix = "-"
    elif 3 <= y <= 6:
        postfix = ""
    elif 7 <= y <= 9:
        postfix = "+"

    print(str(x) + postfix)
