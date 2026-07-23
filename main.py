from password_checker import password_strength
from password_generator import generate_password

while True:
    print("\n===== CyberSec Toolkit =====")
    print("1. Password Strength Checker")
    print("2. Password Generator")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        password = input("Enter password: ")
        password_strength(password)

    elif choice == "2":
        generate_password()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
