import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters  # a-z + A-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&*()_+ etc

    if not characters:
        return "No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input
try:
    length = int(input("Enter password length: "))
    if length <= 0:
        raise ValueError

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")

except ValueError:
    print("Please enter a valid number for password length.")
