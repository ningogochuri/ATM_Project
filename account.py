
from json_manager import read_data, write_data
from transactions import record_transaction
from validators import validate_amount


# აჩვენებს მომხმარებლის მიმდინარე ბალანსს
def check_balance(user):
    print(f"Your current balance: {user['balance']:.2f}")


# ამატებს თანხას მომხმარებლის ანგარიშზე
def deposit(user):
    users = read_data("data/users.json")

    try:
        # ამოწმებს შეყვანილი თანხის სისწორეს
        amount = validate_amount(input("Enter deposit amount: "))

        # ეძებს მომხმარებლის ანგარიშს
        for account in users:
            if account["username"] == user["username"]:
                account["balance"] = round(
                    account["balance"] + amount, 2
                )

                # ინახავს განახლებულ ბალანსს
                if write_data("data/users.json", users):
                    user["balance"] = account["balance"]

                    # ინახავს შესრულებულ ტრანზაქციას
                    record_transaction(
                        user["username"], "deposit", amount
                    )
                    print("Deposit successful!")
                    print(f"New balance: {user['balance']:.2f}")
                else:
                    print("Deposit failed!")

                return

        print("User not found!")

    except ValueError as error:
        print(error)


# აკლებს თანხას მომხმარებლის ანგარიშს
def withdraw(user):
    users = read_data("data/users.json")

    try:
        # ამოწმებს შეყვანილი თანხის სისწორეს
        amount = validate_amount(input("Enter withdrawal amount: "))

        # ეძებს მომხმარებლის ანგარიშს
        for account in users:
            if account["username"] == user["username"]:

                # ამოწმებს, აქვს თუ არა მომხმარებელს საკმარისი თანხა
                if amount > account["balance"]:
                    print("ბალანსი არასაკმარისია!")
                    return

                account["balance"] = round(
                    account["balance"] - amount, 2
                )

                # ინახავს განახლებულ ბალანსს
                if write_data("data/users.json", users):
                    user["balance"] = account["balance"]

                    # ინახავს შესრულებულ ტრანზაქციას
                    record_transaction(
                        user["username"], "withdrawal", amount
                    )
                    print("Withdrawal successful!")
                    print(f"New balance: {user['balance']:.2f}")
                else:
                    print("Withdrawal failed!")

                return

        print("User not found!")

    except ValueError as error:
        print(error)
