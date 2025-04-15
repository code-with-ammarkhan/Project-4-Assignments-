import random
import string

def generate_password(length, use_digits=True, use_symbols=True, use_uppercase=True):
    characters = list(string.ascii_lowercase)
    
    if use_digits:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()-_=+[]{};:,.<>?")
    if use_uppercase:
        characters += list(string.ascii_uppercase)

    if not characters:
        return "No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length <= 0:
                print("Length must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    return length, use_digits, use_symbols, use_uppercase

def main():
    print("=== Password Generator ===")
    length, digits, symbols, uppercase = get_user_preferences()
    password = generate_password(length, digits, symbols, uppercase)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
