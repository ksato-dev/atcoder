from enum import Enum


class ParityType(Enum):
    ODD = 1
    EVEN = 2


def check_parity(value):
    ret_type = None
    if value % 2 == 0:
        ret_type = ParityType.EVEN
    else:
        ret_type = ParityType.ODD

    return ret_type


if __name__ == "__main__":
    a, b, c = [int(v) for v in input().split()]

    other1 = min(a, b)
    max_value = max(a, b)
    other2 = min(max_value, c)
    max_value = max(max_value, c)

    o1_parity = check_parity(other1)
    o2_parity = check_parity(other2)
    max_parity = check_parity(max_value)

    count_ope1 = 0
    if max_parity == o1_parity:
        count_ope1 = (max_value - other1) / 2
    else:
        count_ope1 = (max_value - other1 - 1) / 2
    other1 += int(count_ope1) * 2

    count_ope2 = 0
    if max_parity == o2_parity:
        count_ope2 = (max_value - other2) / 2
    else:
        count_ope2 = (max_value - other2 - 1) / 2
    other2 += int(count_ope2) * 2

    count_ope = int(count_ope1) + int(count_ope2)

    if other1 == other2 == max_value:
        pass
    elif other1 == other2 != max_value:
        count_ope += 1
    elif other1 != other2 == max_value:
        count_ope += 2
    elif other1 == max_value != other2:
        count_ope += 2

    print(count_ope)
