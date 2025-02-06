base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
     'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
     'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c',
     'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
     '7', '8', '9', '+', '/']
base64String=""

text = input("Write what ever you want to encode in Base64: ")
binaryString="".join(format(ord(character), "08b") for character in text)
idx=0
for i in range((len(binaryString)//6)+1):
    temp=binaryString[idx:idx+6]
    base64String+=base64[int(temp,2)]
    idx+=6
remain=len(binaryString)-(idx-6)
if remain>0:
    lastElements=int((6-remain)/2)
    base64String+=base64[int((binaryString[(idx-6):len(binaryString)]+"00"*lastElements),2)]
    base64String+="="*(lastElements)
print(base64String)
