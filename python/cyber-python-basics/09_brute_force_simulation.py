"""Brute Force Simulation: find a password from a small list.

Educational demo only, against a hard-coded local value.
"""
correct_password = "admin123"
passwords = ["123456", "admin", "admin123", "password"]

for pwd in passwords:
    if pwd == correct_password:
        print("Password Found:", pwd)
        break
else:
    print("Password not found")
