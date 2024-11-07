import re

def check_email(email):
    if re.search(r'\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{2,7}\b', email):
        print("Valid email")
    else:
        print("Invalid email")


email = input("Enter email: ")
check_email(email)