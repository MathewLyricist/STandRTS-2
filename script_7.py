def count_patients(file_path, age_limit, city):
    count = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = [field.strip() for field in line.split()]

            if len(data) != 5:
                continue

            surname, gender, age, residence, diagnosis = data

            try:
                age = int(age)
            except ValueError:
                continue

            if age < age_limit and residence.lower() == city.lower():
                count += 1

    return count


if __name__ == "__main__":
    try:
        Y = int(input("Введите возраст (Y): "))
        X = input("Введите город (X): ")

        result = count_patients('klinika.txt', Y, X)

        print(f"Количество пациентов младше {Y} лет из города {X}: {result}")
    except ValueError:
        print("Ошибка ввода: введите корректное значение возраста.")
