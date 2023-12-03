import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        raise ValueError("Password length should be a positive integer.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Generate and display the password (encode to utf-8 to handle potential encoding issues)
password = generate_password(length)
print(f"Generated Password: {password.encode('utf-8', 'replace').decode('utf-8')}")