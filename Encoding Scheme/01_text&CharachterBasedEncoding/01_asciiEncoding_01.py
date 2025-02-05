get=input()
out=""
for i in range(len(get)):
    temp=str(bin(ord(get[i])))
    if len(temp)!=8:
        out+="0"*(8-len(temp[2::]))+temp[2::]
print(len(out))
print(out)