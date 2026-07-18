# Secure password generator
import secrets
import string


# Check whether the password meets all security requirements
def check_password(password):
    
    upper_case = any(char in string.ascii_uppercase for char in password)
    lower_case = any(char in string.ascii_lowercase for char in password)
    digits = any(char in string.digits for char in password)
    special_characters = any(char in string.punctuation for char in password)
    correct_length = len(password) >= 8

    # Store all password checks
    checks = [
        upper_case,
        lower_case,
        digits,
        special_characters,
        correct_length
    ]

    # Return the total password strength score
    return sum(checks)


# Generate a strong password
def generate_password():
    # Create a set of allowed characters
    characters = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

    # Choose a random password length
    length = secrets.randbelow(9) + 8

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    # Generate a new password if the current one is not strong enough
    if check_password(password) < 5:
        return generate_password()

    # Return the strong password
    return password


# Generate and display the password
password = generate_password()

print("Generated password:", password)
print("Password strength:", check_password(password), "/5")

input()