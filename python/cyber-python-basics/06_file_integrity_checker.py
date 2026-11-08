"""File Integrity Checker: generate the hash of a file.

Usage: python 06_file_integrity_checker.py [filename]
"""
import hashlib
import sys


def file_hash(filename: str, algo: str = "sha256") -> str:
    h = hashlib.new(algo)
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
    try:
        print(f"SHA-256 ({name}):", file_hash(name))
    except FileNotFoundError:
        print(f"File not found: {name}")
