def generate_number_powers():
    numbers_and_powers = [[i ** j for j in range(1, 5)] for i in range(1, 6)]

    for i, powers in enumerate(numbers_and_powers, start=1):
        print(f"Число {i}: степени - {powers}")

if __name__ == "__main__":
    generate_number_powers()
