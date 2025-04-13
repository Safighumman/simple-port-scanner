
---

## 🐍 port_scanner.py (Main Script)

```python
import socket
from concurrent.futures import ThreadPoolExecutor
import time

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"[+] Port {port} is OPEN ({service})")
            # else:
            #     print(f"[-] Port {port} is closed")
    except socket.error:
        print(f"[!] Cannot connect to host {host}")
        return

def main():
    print("=== Simple Port Scanner ===")
    host = input("Enter target host (IP or domain): ").strip()
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nTarget IP: {host}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

    end_time = time.time()
    print(f"\nScan complete in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
