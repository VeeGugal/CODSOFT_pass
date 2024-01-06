import random
import string

def generate_password(length):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices
    password = ''.join(random.choices(characters, k=length))
    return password

# Get user input for password length
try:
    password_length = int(input("Enter the desired length of the password you want to create : "))
except ValueError:
    print("Invalid input. Please enter a valid number for the password length so that it will make me easy to create password for you .")
    exit()

# Check if the password length is valid
if password_length <= 0:
    print("Password length you have given is Invalid. Please enter a positive number.")
else:
    # Generate and display the password
    generated_password = generate_password(password_length)
    print(f"Generated Password is as follows: {generated_password}")
