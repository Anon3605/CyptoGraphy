def utf32(text):
    for char in text:
        utf32_bytes = char.encode("utf-32")
        print(f"'{char}' → Unicode: {hex(ord(char))}, UTF-32: {utf32_bytes}, Bytes Used: {len(utf32_bytes)}")
utf32("A é अ 😂")
usrText=input("Give anything you wanna encode: ")
utf32(usrText)