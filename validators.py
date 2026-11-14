
# ამოწმებს მომხმარებლის სახელის სისწორეს
def validate_username(username):
    return bool(username.strip()) and len(username.strip()) >= 3


# ამოწმებს პაროლის მინიმალურ სიგრძეს
def validate_password(password):
    return len(password.strip()) >= 4


# ამოწმებს თანხის სისწორეს და აბრუნებს დამრგვალებულ მნიშვნელობას
def validate_amount(value):
    try:
        # გარდაქმნის შეყვანილ მნიშვნელობას ათწილადად
        amount = float(value)

    except ValueError:
        raise ValueError("Please enter a valid number!")

    # არ უშვებს ნულოვან ან უარყოფით თანხას
    if amount <= 0:
        raise ValueError("Amount must be greater than zero!")

    return round(amount, 2)
