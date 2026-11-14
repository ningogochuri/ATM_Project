
from json_manager import read_data, write_data


# ადმინისტრატორის სატესტო მონაცემები
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


# ამოწმებს ადმინისტრატორის ავტორიზაციის მონაცემებს
def login_admin():
    username = input("Enter admin username: ").strip()
    password = input("Enter admin password: ").strip()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Admin login successful!")
        return True

    print("Invalid admin credentials!")
    return False


# აჩვენებს სისტემაში რეგისტრირებულ ყველა მომხმარებელს
def view_users():
    users = read_data("data/users.json")

    if not users:
        print("No users found.")
        return

    print("\n=== ALL USERS ===")

    for user in users:
        print(f"Username: {user['username']}")
        print(f"Balance: {user['balance']:.2f}")
        print("-" * 30)


# ეძებს მომხმარებელს მისი სახელის მიხედვით
def search_user():
    users = read_data("data/users.json")
    username = input("Enter username to search: ").strip()

    for user in users:
        if user["username"] == username:
            print("\nUser found!")
            print(f"Username: {user['username']}")
            print(f"Balance: {user['balance']:.2f}")
            return

    print("User not found!")


# აახლებს მომხმარებლის ბალანსს
def update_user_balance():
    users = read_data("data/users.json")
    username = input("Enter username: ").strip()

    for user in users:
        if user["username"] == username:
            try:
                new_balance = float(input("Enter new balance: "))

                # არ უშვებს უარყოფითი ბალანსის შეყვანას
                if new_balance < 0:
                    print("Balance cannot be negative!")
                    return

                user["balance"] = round(new_balance, 2)

                # ინახავს განახლებულ მონაცემებს
                if write_data("data/users.json", users):
                    print("Balance updated successfully!")
                else:
                    print("Could not update balance!")

            except ValueError:
                print("Please enter a valid number!")

            return

    print("User not found!")


# შლის მომხმარებელს სისტემიდან
def delete_user():
    users = read_data("data/users.json")
    username = input("Enter username to delete: ").strip()

    for user in users:
        if user["username"] == username:
            # ითხოვს დადასტურებას წაშლამდე
            confirmation = input(
                f"Are you sure you want to delete {username}? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                users.remove(user)

                # ინახავს სიას წაშლის შემდეგ
                if write_data("data/users.json", users):
                    print("User deleted successfully!")
                else:
                    print("Could not delete user!")

            else:
                print("Deletion cancelled!")

            return

    print("User not found!")
