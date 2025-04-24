import requests
import sys
import os

# Ensure the user provides a domain name as an argument
if len(sys.argv) < 2:
    print("Usage: python main.py <domain>")
    sys.exit(1)

# Verify the file path
file_path = "subdomains.txt"
if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

# Read the subdomains from the file
try:
    with open(file_path, "r") as file:
        sub_list = file.read()
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

subdoms = sub_list.splitlines()

# Check subdomains
for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)
    except requests.ConnectionError:
        print(f"Invalid domain: {sub_domains}")
    else:
        print("Valid domain: ", sub_domains)