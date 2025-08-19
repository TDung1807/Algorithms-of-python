# setup
password = input("Create your password: ")
phone_num = input("Enter your phone number: ")

def ask_password(prompt="Password: "):
    return input(prompt)

def verify_phone(expected_phone: str) -> None:
    while True:
        entered = input("Enter your phone number to reset password: ")
        if entered == expected_phone:
            return
        print("Invalid phone number. Try again.")

def new_password() -> str:
    return input("Enter your new password: ")

# auth loop
while True:
    user = ask_password()
    if user == password:
        print("OK")
        break

    print("Invalid password. Try again.")
    choice = input("Press T to try again, R to reset password: ").strip().upper()
    if choice == "T":
        continue
    elif choice == "R":
        verify_phone(phone_num)
        password = new_password()
        print("Password changed. Please log in again.")
    else:
        print("Error!")