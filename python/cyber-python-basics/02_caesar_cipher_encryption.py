"""Caesar Cipher Encryption (letters wrap around A-Z / a-z)."""


def encrypt(text: str, shift: int = 3) -> str:
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


if __name__ == "__main__":
    text = input("Enter Text: ")
    print("Encrypted:", encrypt(text, 3))
