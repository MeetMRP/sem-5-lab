import re

def is_valid_name(name):
    pattern = r"^[A-Za-z\s]+$"
    return bool(re.match(pattern, name))

def is_valid_phone_number(phone):
    pattern = r"^\+?\d{10,15}$"
    return bool(re.match(pattern, phone))

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

# Example usage
name = "Meet Patel"
phone = "67890"
email = "meet@example.com"

if is_valid_name(name) and is_valid_phone_number(phone) and is_valid_email(email):
    print("All inputs are valid.")
else:
    print("Some inputs are invalid.")
