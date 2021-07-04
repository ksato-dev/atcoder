def read_data():
    line = input()
    arr_str = line.split()
    ret_data = map(int, arr_str)

    return ret_data


if __name__ == "__main__":
    A, B, C, X, Y = read_data()

    max_ABC = 5000
    max_XY = int(1e5)
    inf_val = 1e20

    pre_sum_pizzas = inf_val

    """
    [definition]
    x: the number of A-pizza.
    y: the number of B-pizza.
    z: the number of AB-pizza.
    """
    max_z = max(X, Y) * 2
    for z in range(0, max_z + 1, 2):
        x = X - z / 2
        y = Y - z / 2
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        curr_sum_pizzas = A * x + B * y + C * z
        pre_sum_pizzas = min(curr_sum_pizzas, pre_sum_pizzas)

    print(int(pre_sum_pizzas))
