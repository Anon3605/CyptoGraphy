text = "A é अ 😂"

for char in text:
    utf8_bytes = char.encode("utf-8")
    print(f"'{char}' → Unicode: {hex(ord(char))}, UTF-8: {utf8_bytes}, Bytes Used: {len(utf8_bytes)}")
