letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]

my_dict = dict(zip(letters, numbers))

print("Словарь:", my_dict)

total_sum = sum(my_dict.values())
print("Сумма всех значений:", total_sum)

with open("ex2-1.txt", "w") as file:
    file.write(f"Словарь: {my_dict}\n")
    file.write(f"Сумма всех значений: {total_sum}\n")
