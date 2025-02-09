def main():
    min_length = 8
    password = get_valid_password(min_length)
    print_password(password)


def get_valid_password(min_length):
    password = input("Please enter your password: ")
    if len(password) >= min_length:
        return password
    else:
        print(f"Password must be at least {min_length} characters long. Please try again.")


def print_password(password):
    print("*" * len(password))


main()
