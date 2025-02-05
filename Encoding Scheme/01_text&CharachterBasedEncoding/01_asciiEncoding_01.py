get=input("Enter the Text You wanna Encode: ")
out=""
for i in range(len(get)):
    temp=str(bin(ord(get[i])))
    if len(temp)<8:
        out+="0"*(8-len(temp[2::]))+temp[2::]
    else:
        print("The Character you gave doesn't belong to the ASCII Table")
print(f"Encoded ASCII binary String:\n{out}")