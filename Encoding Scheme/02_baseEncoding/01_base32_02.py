import base64

text = "Hello, World!"
encoded = base64.b32encode(text.encode())
decoded = base64.b32decode(encoded).decode()

print("Base32 Encoded:", encoded)
print("Base32 Decoded:", decoded)
