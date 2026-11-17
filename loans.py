from json_manager import read_data, write_data


# მომხმარებლისგან იღებს სესხის მოთხოვნას
def request_loan(user):
    loans = read_data("data/loans.json")

    try:
        amount = float(input("Enter loan amount: "))

        # ამოწმებს, რომ სესხის თანხა დადებითი იყოს
        if amount <= 0:
            print("Loan amount must be greater than zero!")
            return

        # ქმნის ახალ სესხის მოთხოვნას
        new_loan = {
            "username": user["username"],
            "amount": round(amount, 2),
            "status": "pending"
        }

        loans.append(new_loan)

        # ინახავს მოთხოვნას JSON ფაილში
        if write_data("data/loans.json", loans):
            print("Loan request submitted successfully!")
        else:
            print("Could not submit loan request!")

    except ValueError:
        print("Please enter a valid amount!")


# აჩვენებს ყველა სესხის მოთხოვნას
def view_loan_requests():
    loans = read_data("data/loans.json")

    if not loans:
        print("No loan requests found.")
        return

    print("\n=== LOAN REQUESTS ===")

    # enumerate გვაძლევს როგორც ინდექსს, ისე მოთხოვნის მონაცემებს
    for index, loan in enumerate(loans):
        print(f"ID: {index}")
        print(f"Username: {loan['username']}")
        print(f"Amount: {loan['amount']:.2f}")
        print(f"Status: {loan['status']}")
        print("-" * 30)


# ადმინისტრატორი ამტკიცებს ან უარყოფს სესხის მოთხოვნას
def process_loan():
    loans = read_data("data/loans.json")

    if not loans:
        print("No loan requests found.")
        return

    view_loan_requests()

    try:
        loan_id = int(input("Enter loan ID: "))

        # ამოწმებს, არსებობს თუ არა მითითებული მოთხოვნის ID
        if loan_id < 0 or loan_id >= len(loans):
            print("Invalid loan ID!")
            return

        loan = loans[loan_id]

        # ამოწმებს, ხომ არ არის მოთხოვნა უკვე დამუშავებული
        if loan["status"] != "pending":
            print("This request has already been processed!")
            return

        decision = input(
            "Approve or reject? (approve/reject): "
        ).strip().lower()

        if decision == "approve":
            users = read_data("data/users.json")

            target_user = None

            # ეძებს მომხმარებელს, რომელმაც სესხი მოითხოვა
            for user in users:
                if user["username"] == loan["username"]:
                    target_user = user
                    break

            if target_user is None:
                print("User not found!")
                return

            # ამატებს დამტკიცებულ სესხს მომხმარებლის ბალანსს
            target_user["balance"] = round(
                target_user["balance"] + loan["amount"], 2
            )

            loan["status"] = "approved"

            # ინახავს სესხის დამტკიცებულ სტატუსს
            if not write_data("data/loans.json", loans):
                print("Could not save loan approval!")
                return

            # ინახავს მომხმარებლის განახლებულ ბალანსს
            if not write_data("data/users.json", users):
                print("Could not update user balance!")
                loan["status"] = "pending"
                write_data("data/loans.json", loans)
                return

            print("Loan approved successfully!")
            print(f"New balance: {target_user['balance']:.2f}")

        elif decision == "reject":
            # უარყოფს სესხის მოთხოვნას
            loan["status"] = "rejected"

            if write_data("data/loans.json", loans):
                print("Loan rejected!")
            else:
                print("Could not save loan rejection!")

        else:
            print("Invalid decision!")

    except ValueError:
        print("Please enter a valid loan ID!")
