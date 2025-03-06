def calc(expression):
    expression = expression.replace('%', '/100')

    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка при вычислении: {e}"


if __name__ == "__main__":
    print(calc('1 + 9'))
    print(calc('50% + 50'))
    print(calc('2 ** 3'))
    print(calc('5 + 15%'))
    print(calc('4 ** 0.5'))
