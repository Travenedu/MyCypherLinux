t = input("How many shifts\n")
s = int(t)
text = input("What is your message?\n")
def encrypt(text,s):
    str = ""
    desi = []
    final = []
    CAP = text.upper()
    for i in CAP:
        desi.append(i)
    for i in desi:
        if i == " " or i == ' ' or i == "`" or i == "~" or i == "!" or i == "@" or i == "#" or i == "$" or i == "%":
            desi.remove(i)
        if i == "^" or i == "&" or i == "*" or i == "(" or i == ")" or i == "_" or i == "-" or i == "+":
            desi.remove(i)
        if i == "=" or i == "{" or i == "}" or i == "[" or i == "]" or i == "|" or i == "" or i == ":":
            desi.remove(i)
        if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8":
            desi.remove(i)
        if i == "9" or i == "0" or i == ";" or i == "<" or i == ">" or i == "?" or i == "/":
            desi.remove(i)
        if i == "," or i == ".":
            desi.remove(i)
    for i in desi:
        if i == " ":
            desi.remove(i)
    result = ""
    for i in range(len(desi)):
        character = desi[i]
        result += chr((ord(character) + s-65) % 26 + 65)
    for i in result:
        final.append(i)
    space = 4
    q = 0
    while q < len(final):
        if q < 3:
            space = 5
        else:
            space = space + 2
        final.insert(space, " ")
        space += 4
        q += 4
    return str.join(final)
print(encrypt(text, s))
