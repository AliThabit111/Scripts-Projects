"""Password Strength Checker.

A password is strong if it has at least 8 characters, including an
uppercase letter, a lowercase letter and a digit.
"""
import getpass


def is_strong(password: str) -> bool:
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
    )


if __name__ == "__main__":
    pwd = getpass.getpass("Enter Password: ")
    print("Strong Password" if is_strong(pwd) else "Weak Password")
