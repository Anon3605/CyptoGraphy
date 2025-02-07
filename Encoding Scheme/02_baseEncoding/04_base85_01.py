base85=[
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', '!', '#', '$', '%', '&', '(', ')', '*',
    '+', '-', ';', '<', '=', '>', '?', '@', '^', '_',
    '`', '{', '|', '}', '~'
]
def asciiBytes():
    hexCode=[hex(character) for character in bytearray
        (input("Enter the text you want to encode in Base85: ").encode())]
    merger4(hexCode)

def merger4(hexCode,bytesList=[]):
    idx=0
    while idx<len(hexCode)-4:
        combineHex="0x"
        for hexC in range(idx,idx+4):
            combineHex+=hexCode[hexC][2::]
        bytesList.append(combineHex)
        idx+=4
    if len(bytesList)%4!=0:
        combineHex=""
        for hexC in range(1,len(bytesList)%4+1):
            combineHex+=hexCode[-hexC][-1:-3:-1]
        combineHex+="x0"
        bytesList.append(combineHex[-1::-1]+("00"*(4-len(bytesList)%4)))
    b58encode(bytesList)

def b58encodeOperation(encode):
    n0=int((encode/52200625)%85)+33
    n1=int((encode/614125)%85)+33
    n2=int((encode/7225)%85)+33
    n3=int((encode/85)%85)+33
    n4=int((encode/1)%85)+33
    return [n0,n1,n2,n3,n4]

def b58encode(byteList):
    encodeString=""
    for element in byteList:
        encode=int(element, 16)
        encodeList=b58encodeOperation(encode)
        encodeString+="".join(chr(i) for i in encodeList)
    print(encodeString)

asciiBytes()

