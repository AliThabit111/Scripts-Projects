"""IPv4 Address Validator."""
import ipaddress


def is_valid_ipv4(ip: str) -> bool:
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    ip = input("Enter IP: ").strip()
    print("Valid IP" if is_valid_ipv4(ip) else "Invalid IP")
