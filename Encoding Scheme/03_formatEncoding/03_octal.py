text=input("Give the text you want to convert in octal: ")
print("""As we know there are some title called padding which actually adds
zeros before the actual octal so that we can differ the characters
that in the octal string.""")
padding=int(input("Give the length of each octal values for characters: "))
encodedText=""
for i in text:
    encodedText+="".join(format(ord(i),f"0{padding}o"))
print(encodedText)