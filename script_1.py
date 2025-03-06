def is_palindrome(s):
    s = s.replace(" ", "").lower()
    reversed_s = "".join(reversed(s))
    return s == reversed_s


def main():
    user_input = input("Введите строку: ")

    if is_palindrome(user_input):
        print(f'"{user_input}" является палиндромом.')
    else:
        print(f'"{user_input}" не является палиндромом.')


if __name__ == "__main__":
    main()
