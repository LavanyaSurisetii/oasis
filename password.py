import random
import string

def generate_password(length, has_letters, has_numbers, has_symbols):
    password = ''
    char_set = ''

    if has_letters:
        char_set += string.ascii_letters
    if has_numbers:
        char_set += string.digits
    if has_symbols:
        char_set += string.punctuation

    for _ in range(length):
        password += random.choice(char_set)

    return password

def main():
    print("Password Generator")
    print("----------------")

    length = int(input("Enter password length: "))

    has_letters = input("Include letters? (y/n): ").lower() == 'y'
    has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    has_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, has_letters, has_numbers, has_symbols)

    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
    