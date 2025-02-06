import base64

text = "Hello, World!"
encoded = base64.b85encode(text.encode())
decoded = base64.b85decode(encoded).decode()

print("Base85 Encoded:", encoded)
print("Base85 Decoded:", decoded)
