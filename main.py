# შემოაქვს მომხმარებლის რეგისტრაციისა და ავტორიზაციის ფუნქციები
from auth import register_user, login_user

# შემოაქვს ანგარიშის მართვის ფუნქციები
from account import check_balance, deposit, withdraw

# შემოაქვს ტრანზაქციების ისტორიის ფუნქცია
from transactions import view_transactions

# შემოაქვს ადმინისტრატორის ფუნქციები
from admin import (
    login_admin,
    view_users,
    search_user,
    update_user_balance,
    delete_user
)

# შემოაქვს სესხების მართვის ფუნქციები
from loans import (
    request_loan,
    view_loan_requests,
    process_loan
)


# მომხმარებლის მენიუ
def client_menu(user):
    while True:
        print("\n=== ATM CLIENT MENU ===")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction history")
        print("5. Request loan")
        print("6. Logout")

        choice = input("Choose an option: ").strip()

        # ასრულებს მომხმარებლის მიერ არჩეულ მოქმედებას
        if choice == "1":
            print("\nChecking balance...")
            check_balance(user)

        elif choice == "2":
            deposit(user)

        elif choice == "3":
            withdraw(user)

        elif choice == "4":
            view_transactions(user["username"])

        elif choice == "5":
            request_loan(user)

        elif choice == "6":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice! Try again.")


# ადმინისტრატორის მენიუ
def admin_menu():
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. View all users")
        print("2. Search user")
        print("3. Update user balance")
        print("4. Delete user")
        print("5. View loan requests")
        print("6. Process loan")
        print("7. Logout")

        choice = input("Choose an option: ").strip()

        # იძახებს შესაბამის ადმინისტრატორის ფუნქციას
        if choice == "1":
            view_users()

        elif choice == "2":
            search_user()

        elif choice == "3":
            update_user_balance()

        elif choice == "4":
            delete_user()

        elif choice == "5":
            view_loan_requests()

        elif choice == "6":
            process_loan()

        elif choice == "7":
            print("Admin logged out!")
            break

        else:
            print("Invalid choice! Try again.")


# მომხმარებლისა და ადმინისტრატორის შესვლის მენიუ
def login_menu():
    while True:
        print("\n====== LOGIN MENU ======")
        print("1. Client Login")
        print("2. Admin Login")
        print("3. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            user = login_user()

            # წარმატებული შესვლის შემთხვევაში ხსნის მომხმარებლის მენიუს
            if user:
                client_menu(user)

        elif choice == "2":
            # წარმატებული ადმინისტრატორის შესვლის შემთხვევაში ხსნის მის მენიუს
            if login_admin():
                admin_menu()

        elif choice == "3":
            break

        else:
            print("Invalid choice! Try again.")


# პროგრამის მთავარი ფუნქცია
def main():
    while True:
        print("\n====== ATM SYSTEM ======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            login_menu()

        elif choice == "3":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice! Try again.")


# პროგრამას უშვებს მხოლოდ მაშინ, როცა ეს ფაილი პირდაპირ გაეშვება
if __name__ == "__main__":
    main()
