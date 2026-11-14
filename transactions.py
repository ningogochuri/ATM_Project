
from datetime import datetime

from json_manager import read_data, write_data


# ინახავს მომხმარებლის მიერ შესრულებულ ტრანზაქციას
def record_transaction(username, transaction_type, amount):
    transactions = read_data("data/transactions.json")

    # ქმნის ახალი ტრანზაქციის ჩანაწერს
    new_transaction = {
        "username": username,
        "type": transaction_type,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    transactions.append(new_transaction)

    # ინახავს ტრანზაქციას JSON ფაილში
    if write_data("data/transactions.json", transactions):
        return True

    return False


# აჩვენებს კონკრეტული მომხმარებლის ტრანზაქციების ისტორიას
def view_transactions(username):
    transactions = read_data("data/transactions.json")

    # ფილტრავს მხოლოდ ამ მომხმარებლის ტრანზაქციებს
    user_transactions = [
        transaction for transaction in transactions
        if transaction["username"] == username
    ]

    if not user_transactions:
        print("No transactions found.")
        return

    print("\n=== TRANSACTION HISTORY ===")

    # აჩვენებს თითოეული ტრანზაქციის დეტალებს
    for transaction in user_transactions:
        print(f"Type: {transaction['type']}")
        print(f"Amount: {transaction['amount']:.2f}")
        print(f"Date: {transaction['date']}")
        print("-" * 30)
