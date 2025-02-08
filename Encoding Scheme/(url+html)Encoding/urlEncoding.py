urlEncode={
    ":" :	"%3A",
    "/" :	"%2F",
    "?" :	"%3F",
    "#" :	"%23",
    "[" :	"%5B",
    "]" :	"%5D",
    "@" :	"%40",
    "!" :	"%21",
    "$" :	"%24",
    "&" :	"%26",
    "'" :	"%27",
    "(" :	"%28",
    ")" :	"%29",
    "*" :	"%2A",
    "+" :	"%2B",
    "," :	"%2C",
    ";" :	"%3B",
    "=" :	"%3D",
    "%" :	"%25",
    " " :	"%20"
}

url=input("Enter the URL to encode: ")
encoded=""
for i in url:
    if i in urlEncode or i=="\"":
        try:
            encoded+=urlEncode[i]
        except:
            encoded+='%27'
        continue
    encoded+=i

print(encoded)