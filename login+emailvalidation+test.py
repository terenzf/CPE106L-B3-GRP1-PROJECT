def loginSystem():
    while True:
        email = input("Enter your email:")
        if (email_validation(email)):
            print("Your Email Address is valid")
            break
        else:
            print("Your email address is invalid please try again!")

    while True:
        password = input("Enter your password:")
        if (len(password) >= 8 and len(password) <= 16):
            print("Your Password is valid")
            break
        else:
            print("Your Password is invalid! Please try again!")


def email_validation(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(pattern, email)


def test():
    email = input("Enter email:")