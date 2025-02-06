import base64

text = "Hello, World!"
encoded = base64.b58encode(text.encode())
decoded = base64.b58decode(encoded).decode()

print("Base58 Encoded:", encoded)
print("Base58 Decoded:", decoded)
