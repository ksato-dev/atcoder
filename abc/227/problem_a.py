if __name__ == "__main__":
    n, k, a = [int(v) for v in input().split()]

    num_rest_cards = k - 1
    person_id = a
    while num_rest_cards > 0:
        if person_id < n:
            person_id = person_id + 1
        elif n <= person_id:
            person_id = 1

        num_rest_cards = num_rest_cards - 1
    print(person_id)
