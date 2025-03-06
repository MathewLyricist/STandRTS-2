def round_number(num, decimal_places):
    return round(num, decimal_places)


def process_numbers(numbers):
    rounded_numbers = list(map(lambda x: round_number(x[0], x[1]), zip(numbers, range(5, 0, -1))))
    return rounded_numbers


def is_greater_than(value, threshold):
    return value > threshold


if __name__ == "__main__":
    m = [3.46871, 5.31916, 4.013449, 6.57686, 15.012678]

    rounded_numbers = process_numbers(m)
    print("Округленные числа:", rounded_numbers)

    threshold = 5
    filtered_numbers = list(filter(lambda x: is_greater_than(x, threshold), rounded_numbers))
    print(f"Числа больше {threshold}:", filtered_numbers)
