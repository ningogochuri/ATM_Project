import hashlib
import secrets

from json_manager import read_data, write_data
from validators import validate_username, validate_password


# პაროლს ქმნის უსაფრთხო ჰეშად უნიკალური salt-ის გამოყენებით
def hash_password(password):
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )

    return salt.hex(), password_hash.hex()


# ამოწმებს შეყვანილი პაროლი ემთხვევა თუ არა შენახულ ჰეშს
def verify_password(password, salt, stored_hash):
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        600000
    )

    return secrets.compare_digest(password_hash.hex(), stored_hash)


# არეგისტრირებს ახალ მომხმარებელს
def register_user():
    users = read_data("data/users.json")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # ამოწმებს მომხმარებლის სახელსა და პაროლს
    if not validate_username(username):
        print("Username must contain at least 3 characters!")
        return

    if not validate_password(password):
        print("Password must contain at least 4 characters!")
        return

    # ამოწმებს, ხომ არ არსებობს ასეთი მომხმარებელი
    for user in users:
        if user["username"] == username:
            print("Username already exists!")
            return

    salt, password_hash = hash_password(password)

    # ქმნის ახალი მომხმარებლის მონაცემებს
    new_user = {
        "username": username,
        "salt": salt,
        "password_hash": password_hash,
        "balance": 0,
        "role": "client"
    }

    users.append(new_user)

    # ინახავს ახალ მომხმარებელს JSON ფაილში
    if write_data("data/users.json", users):
        print("Registration successful!")
    else:
        print("Registration failed!")


# ამოწმებს მომხმარებლის მონაცემებს და ახორციელებს შესვლას
def login_user():
    users = read_data("data/users.json")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # ეძებს მომხმარებელს და ამოწმებს მის პაროლს
    for user in users:
        if user["username"] == username and verify_password(
            password,
            user["salt"],
            user["password_hash"]
        ):
            print("Login successful!")
            return user

    print("Invalid username or password!")
    return None