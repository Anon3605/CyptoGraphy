import html

def htmlEncoder(htmlCode):
    htmlEncode={
    " ":	"&nbsp",
    "<":	"&lt",
    ">":	"&gt",
    "&":	"&amp",
    "\"":	"&quot",
    "'":	"&apos",
    "¢":	"&cent",
    "£":	"&pound",
    "¥":	"&yen",
    "€":	"&euro",
    "©":	"&copy",
    "®":	"&reg",
    }
    encoded=""
    for i in htmlCode:
        if i in htmlEncode:
            encoded+=htmlEncode[i]
            continue
        encoded+=i
    return encoded

def usingModule(htmlCode):
    encoded = html.escape(htmlCode)
    decoded = html.unescape(encoded)
    return (encoded, decoded)

print("The first function shows the functionality how HTML codes are replaced \n    \"WHICH IS NOT COMPLETE\"")
print("The second function shows the the module to encode the html and decode it")
htmlCode=input("Enter the HTML code you want to encode:\n")
print(htmlEncoder(htmlCode))
collection=usingModule(htmlCode)
for i in range(len(collection)):
    print(f"Encoded HTML\n: {collection[i]}") if i==0 else print(f"Decoded HTML\n: {collection[i]}")