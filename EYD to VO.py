#Ejaan Yang Disempurnakan to Ejaan Van Ophuijsen

def changesingleconsonant(msg):
    out = ""
    for x in msg:
        if x == "y":
            x = "j"
        elif x == "u":
            x = "oe"
        elif x  == "c":
            x = "tj"
        elif x  == "j":
            x = "dj"
        out = out + x
    return out

def changedoubleconsonant(msg):
    out = ""
    wordlist = []
    for x in msg:
        wordlist.append(x)
    print(wordlist)
    loop = 0
    for x in range(len(wordlist)):
        vocal = ""
        letter=wordlist[x]
        loop = loop + 1
        if loop > 1:
            loop = 0
            out = out + vocal
            print(vocal)
    print(out)

changedoubleconsonant("halo bang nizar")
