import itertools

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    cards = [int(input()) for _ in range(n)]

    cards_set = set()
    for curr_cards_perm in itertools.permutations(cards, k):
        cards_perm_str = ""
        for num in curr_cards_perm:
            cards_perm_str = cards_perm_str + str(num)
        cards_set.add(cards_perm_str)

    print(len(cards_set))
