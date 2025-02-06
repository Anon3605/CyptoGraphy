import base64

text = input("Write what ever you want to encode in Base64: ")
encoded = base64.b64encode(text.encode())  # Encoding
decoded = base64.b64decode(encoded).decode()  # Decoding

print("Base64 Encoded:", encoded)
print("Base64 Decoded:", decoded)
