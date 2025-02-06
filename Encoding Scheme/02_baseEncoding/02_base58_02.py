import base58

text = input("Write what ever you want to encode in Base58: ")
encoded = base58.b58encode(text.encode())
decoded = base58.b58decode(encoded).decode()

print("Base58 Encoded:", encoded)
print("Base58 Decoded:", decoded)
