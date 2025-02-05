text=input("Give the text you want to convert in hexadecimal: ")
print("""As we know there are some title called padding which actually adds
zeros before the actual hex so that we can differ the characters
that in the hex string.""")
padding=int(input("Give the length of each hex values for characters: "))
encodedText=""
for i in text:
    encodedText+="".join(format(ord(i),f"0{padding}x"))
print(encodedText)