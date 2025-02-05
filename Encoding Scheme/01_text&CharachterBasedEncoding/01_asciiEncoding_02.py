get = input("Enter the Text You wanna Encode: ")
try:
    out = ''.join(format(ord(char), '08b') for char in get)
except:
    print("The Character you gave doesn't belong to the ASCII Table")
print(out)
