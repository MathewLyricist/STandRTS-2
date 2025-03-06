def round_number(num, decimal_places):
    return round(num, decimal_places)


def process_numbers(numbers):
    rounded_numbers = list(map(lambda x: round_number(x[0], x[1]), zip(numbers, range(5, 0, -1))))
    return rounded_numbers


if __name__ == "__main__":
    m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]

    result = process_numbers(m)

    print("Округленные числа:", result)
