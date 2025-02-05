get = input("Enter text: ")
out = ''.join(format(ord(char), '08b') for char in get)

print(len(out))
print(out)
