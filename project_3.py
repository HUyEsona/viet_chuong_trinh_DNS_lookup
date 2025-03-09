import socket
import sys

def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"ten mieng {domain}")
        print(f"dia chi ip {ip_address}")
    except socket.gaierror:
        print(f"Khong the tim thay dia chi IP cho ten mien {domain}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        domain_name = sys.argv[1]
    else:
        domain_name = input("Nhap ten mien can tim dia chi IP: ")
    dns_lookup(domain_name)
        