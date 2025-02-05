def ROT13(text,encoded=""):
    for i in text:
        if ord(i) in range(65,91):
            idx=(ord(i.lower())+13)%123
            if idx<97:
                idx+=97
            encoded+=chr(idx).upper()
        elif ord(i) in range(97,123):
            idx=(ord(i)+13)%123
            if idx<97:
                idx+=97
            encoded+=chr(idx)
        else:
            encoded+=i
    return encoded

text=input("Enter anything you want: ")
encoded=ROT13(text)
print(encoded)