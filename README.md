# 🌐 Simple Port Scanner

This is a lightweight Python script to scan open TCP ports on a given host. It's great for beginners who want to understand how port scanning works under the hood without relying on tools like Nmap.

## ⚙️ Features

- Scans a target IP/domain over a range of ports
- Shows open ports with service names (when available)
- Fast scanning using multithreading
- Supports custom port range input

---

## 🚀 How to Use

1. Clone the repo:

#```bash
git clone https://github.com/yourusername/simple-port-scanner.git
cd simple-port-scanner



2. Install any required packages:

pip install -r requirements.txt



3. Run the script:

python3 port_scanner.py



4. Enter a target host and port range when prompted.


---


## 📸 Example Output

Target IP: 8.8.8.8
Scanning ports from 20 to 100...

[+] Port 22 is OPEN (ssh)
[+] Port 53 is OPEN (domain)
[+] Port 80 is CLOSED
[+] Port 443 is OPEN (https)
Scan complete.

---

## 🛑 Disclaimer
This tool is intended for educational purposes only. Only scan hosts you own or have explicit permission to analyze.


---

## 🧠 Educational Value
This scanner is a great starting point to:

Understand TCP/IP basics

Learn how sockets work in Python

See the difference between open/closed ports

Practice ethical cybersecurity habits

---

## ⭐ Show Support
If you found this useful, give it a ⭐ and check out other projects on my GitHub profile.
