base32 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
     'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
     'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4',
     '5', '6', '7']
# Using string in base32 instead of list is much more faster
# and optimized
base32String=""

text = input("Write what ever you want to encode in Base32: ")
binaryList=[]
for character in text:
    binaryList.append(format(ord(character), "08b"))
remain=len(binaryList)%3
if len(binaryList)%3!=0 and len(binaryList)/3>len(binaryList)//3:
    binaryList.extend(["00000000"]*(3-remain))
if len(binaryList)%3!=0 and len(binaryList)/3<len(binaryList)//3:
    binaryList.extend(["00000000"]*(3-remain))
binaryString="".join(character for character in binaryList)
idx=len(binaryString)-1
for i in range(len(binaryString)//5-1):
    temp=binaryString[idx:idx-5:-1][::-1]
    if temp=="00000":
        # print("Hello")
        base32String+="="
        idx-=5
        continue
    base32String+=base32[int(temp,2)]
    idx-=5
base32String+=base32[int(binaryString[0:5],2)]
print(base32String[::-1])


