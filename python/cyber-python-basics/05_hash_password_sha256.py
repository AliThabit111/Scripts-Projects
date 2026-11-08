"""Convert a password into a SHA-256 hash.

Note: plain SHA-256 is for learning only. For storing real passwords use
bcrypt, scrypt or argon2 with a salt.
"""
import getpass
import hashlib

if __name__ == "__main__":
    password = getpass.getpass("Enter Password: ")
    print(hashlib.sha256(password.encode()).hexdigest())
