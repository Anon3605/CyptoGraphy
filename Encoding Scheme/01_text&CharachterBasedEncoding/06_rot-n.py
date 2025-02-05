def ROT13(text,shift,encoded=""):
    for i in text:
        if ord(i) in range(65,91):
            idx=(ord(i.lower())+shift)%123
            if idx<97:
                idx+=97
            encoded+=chr(idx).upper()
        elif ord(i) in range(97,123):
            idx=(ord(i)+shift)%123
            if idx<97:
                idx+=97
            encoded+=chr(idx)
        else:
            encoded+=i
    return encoded

text=input("Enter anything you want: ")
shifting=int(input("How much ya'll shifting cuz?: "))%26
encoded=ROT13(text, shifting)
print(encoded)