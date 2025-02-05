text = "A é अ 😂"
def utf16(text):
    for char in text:
        utf16_bytes = char.encode("utf-16")
        print(f"'{char}' → Unicode: {hex(ord(char))}, UTF-16: {utf16_bytes}, Bytes Used: {len(utf16_bytes)}")
utf16("A é अ 😂")
usrText=input("Give anything you wanna encode: ")
utf16(usrText)