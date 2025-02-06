import base64

text = "Hello, World!"
encoded = base64.b64encode(text.encode())  # Encoding
decoded = base64.b64decode(encoded).decode()  # Decoding

print("Base64 Encoded:", encoded)
print("Base64 Decoded:", decoded)
