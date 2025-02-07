base58 = ['1', '2', '3', '4', '5', '6', '7', '8',
     '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
     'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
     'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
     'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z']

# def recursion(plainString): #This one just gives you the total value
#     if len(plainString)==1:
#         return ord(plainString[-len(plainString)])*(2**((len(plainString)-1)*8))
#     return ord(plainString[-len(plainString)])*(2**((len(plainString)-1)*8))+recursion(plainString[1::])

def recursion(plainString):
    total=0
    for i in range(len(plainString)):
        total+=ord(plainString[-(i+1)])*(2**(i*8))
    print(total)
    return total

# def recursion02(total,listFinal): #This one do the modulo operations
#     if total%58==0:
#         return listFinal
#     recursion02(total//58,listFinal)
#     return listFinal.append(total%58)

def recursion02(total,listFinal):
    while total%58!=0:
        listFinal.append(total%58)
        total=total//58

total,remainderList=recursion(input("Give any text to convert into base58 ma homie: ")),[]
recursion02(total,remainderList)
remainderList.reverse()
for values in remainderList:
    print(base58[values],end="")