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
    loop = 0
    wordlist = list(msg)
    
    print(wordlist)
    if len(wordlist)%2 != 0:
        wordlist.append(" ")
    
    semiout = ""
    for x in range(len(wordlist)):
        if x%2 == 0:
            x = wordlist[x]+wordlist[x+1]
            if x == "kh":
                x = "ch"
            elif x == "i ":
                x = "ï "
            semiout = semiout+x
    
    wordlist = list(semiout)
    wordlist.append(" ")
    for x in range(len(wordlist)-1):
        if x%2 != 0:
            x = wordlist[x]+wordlist[x+1]
            print(x)
            if x == "kh":
                x = "ch"
            elif x == "i ":
                x = "ï "
            out = out+x
    out=wordlist[0] + out
    print(out)

def changetripleconsonant(msg):
    out = ""
    wordlist = []
    loop = 0
    wordlist = list(msg)
    

    x = len(wordlist)%3
    print(x)
    if x == 1:
        wordlist.append(" ")
        wordlist.append(" ")
    elif x != 0:
        wordlist.append(" ")
    
    print(wordlist, len(wordlist))

    semiout = ""
    for x in range(len(wordlist)):
        if x%3 == 0:
            x = wordlist[x]+wordlist[x+1]+wordlist[x+2]
            #5print(x)
            if x in ["aka", "aki", "aku", "ake", "ako"]:
                x = "a'"
            semiout = semiout+x


    wordlist.append(" ")
    for x in range(len(wordlist)):
        if x%3 == 1:
            x = wordlist[x]+wordlist[x+1]
            y = wordlist[x+2]
            #print(x)
            if x == "ak":
                x = "a'"
            out = out+x


    print(out)

changetripleconsonant("makanan maklum makin mikir iklim ukuran ukraina")

