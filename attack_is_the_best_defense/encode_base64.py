#!/usr/bin/python3
import base64
import sys

if len(sys.argv) < 2:
    print("Please provide a string as an argument.")
    sys.exit(1)

string_to_encode = sys.argv[1]

try:
    encoded_bytes = base64.b64encode(string_to_encode.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    print("Base64 encoded string: ", encoded_string)
except Exception as e:
    print("Error encoding string:", str(e))
