import json
import os

ADMIN_FILE = "admin.json"


def admin_login():

    if not os.path.exists(ADMIN_FILE):

        admin = {
            "username": "admin",
            "password": "admin123"
        }

        with open(ADMIN_FILE, "w") as file:
            json.dump(admin, file, indent=4)

    with open(ADMIN_FILE, "r") as file:
        admin = json.load(file)

    print("\n" + "=" * 40)
    print("          ADMIN LOGIN")
    print("=" * 40)

    username = input("Username : ")
    password = input("Password : ")

    if username == admin["username"] and password == admin["password"]:
        print("\nLogin Successful!\n")
        return True

    print("\nInvalid Username or Password!")
    return False

def change_admin_password():

    with open(ADMIN_FILE, "r") as file:
        admin = json.load(file)

    print("\n" + "=" * 40)
    print("      CHANGE ADMIN PASSWORD")
    print("=" * 40)

    username = input("Enter Username : ")

    old_password = input("Enter Old Password : ")

    if username != admin["username"] or old_password != admin["password"]:
        print("\nInvalid Username or Password.")
        return

    new_password = input("Enter New Password : ")

    confirm_password = input("Confirm New Password : ")

    if new_password != confirm_password:
        print("\nPasswords do not match.")
        return

    admin["password"] = new_password

    with open(ADMIN_FILE, "w") as file:
        json.dump(admin, file, indent=4)

    print("\nPassword Changed Successfully.")
