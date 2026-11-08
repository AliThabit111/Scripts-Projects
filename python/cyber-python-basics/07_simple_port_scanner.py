"""Simple Port Scanner: check whether a single port is open.

Only scan hosts you own or have permission to test.
"""
import socket


def is_port_open(host: str, port: int, timeout: float = 2.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


if __name__ == "__main__":
    host = "google.com"
    port = 80
    print("Port Open" if is_port_open(host, port) else "Port Closed")
