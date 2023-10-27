import random
import string

def generate_password():
    num_chars = int(input("Enter the number of characters in the password: "))
    num_uppercase = int(input("Enter the number of uppercase letters: "))
    num_lowercase = int(input("Enter the number of lowercase letters: "))
    num_digits = int(input("Enter the number of digits: "))
    num_special_chars = int(input("Enter the number of special characters: "))

    if num_chars < (num_uppercase + num_lowercase + num_digits + num_special_chars):
        print("Invalid input. The total number of characters must be at least as many as the sum of uppercase, lowercase, digits, and special characters.")
        return

    password = ""

    for _ in range(num_uppercase):
        password += random.choice(string.ascii_uppercase)

    for _ in range(num_lowercase):
        password += random.choice(string.ascii_lowercase)

    for _ in range(num_digits):
        password += random.choice(string.digits)

    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?~"
    for _ in range(num_special_chars):
        password += random.choice(special_chars)

    remaining_chars = num_chars - len(password)
    for _ in range(remaining_chars):
        password += random.choice(string.ascii_letters + string.digits + special_chars)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Generated Password: ", password)

if __name__ == "__main__":
    generate_password()
