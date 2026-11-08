"""Generate a secure random password using the `secrets` module."""
import secrets
import string


def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(secrets.choice(chars) for _ in range(length))


if __name__ == "__main__":
    print(generate_password(12))
