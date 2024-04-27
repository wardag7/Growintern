import re

def test_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Weak"

    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Weak"

    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Weak"

    # Check for digits
    if not re.search("[0-9]", password):
        return "Weak"

    # Check for special characters
    if not re.search("[!@#$%^&*()-_+=]", password):
        return "Weak"

    return "Strong"

def main():
    while True:
        password = input("Enter your password: ")
        strength = test_password_strength(password)
        if strength == "Strong":
            print("Password strength: Strong")
            break
        else:
            print("Password strength: Weak. Please enter a stronger password.")

if __name__ == "__main__":
    main()
