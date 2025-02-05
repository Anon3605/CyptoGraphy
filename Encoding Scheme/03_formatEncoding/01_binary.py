text=input("Give the text you want to convert in binary: ")
print("""As we know there are some title called padding which actually adds
zeros before the actual binary so that we can differ th characters
that in the binary string.""")
padding=int(input("Give the length of each binary values for characters: "))
encodedText=""
for i in text:
    encodedText+="".join(format(ord(i),f"0{padding}b"))
print(encodedText)