#!/usr/bin/python3
import base64
import sys

if len(sys.argv) < 2:
    print("Please provide a base64-encoded password as an argument.")
    sys.exit(1)

encoded_password = sys.argv[1]

try:
    decoded_password = base64.b64decode(encoded_password).decode('utf-8')
    print("Decoded password:", decoded_password)
except Exception as e:
    print("Error decoding the password:", str(e))
