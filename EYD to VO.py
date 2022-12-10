#Ejaan Yang Disempurnakan to Ejaan Van Ophuijsen
import pyperclip

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
    
    if len(wordlist)%2 != 0:
        wordlist.append(" ")
    
    semiout = ""
    for x in range(len(wordlist)): #*first loop
        if x%2 == 0:
            x = wordlist[x]+wordlist[x+1]
            if x == "kh":
                x = "ch"
            elif x == "i ":
                x = "ï "
            semiout = semiout+x
    
    wordlist = list(semiout)
    wordlist.append(" ")
    for x in range(len(wordlist)-1): #*second loop
        if x%2 != 0:
            x = wordlist[x]+wordlist[x+1]
            if x == "kh":
                x = "ch"
            elif x == "i ":
                x = "ï "
            out = out+x
    out=wordlist[0] + out
    return out

def changetripleconsonant(msg):
    out = ""
    wordlist = []
    loop = 0
    wordlist = list(msg)
    

    x = len(wordlist)%3
    if x == 1:
        wordlist.append(" ")
        wordlist.append(" ")
    elif x != 0:
        wordlist.append(" ")
    
    semiout = ""
   
    for x in range(len(wordlist)): #*first loop
        if x%3 == 0:
            last = wordlist[x+2]
            x = wordlist[x]+wordlist[x+1]+wordlist[x+2]
            if x in ["akb", "akc", "akd", "akf", "akg", "akh", "akj", "akk", "akl", "akm", "akn", 
                    "akp", "akq", "akr", "aks", "akt", "akv", "akw", "akx", "aky", "akz", "ak "]:
                x = "a`"
                x = x + last
            if x in ["ikb", "ikc", "ikd", "ikf", "ikg", "ikh", "ikj", "ikk", "ikl", "ikm", "ikn", 
                    "ikp", "ikq", "ikr", "iks", "ikt", "ikv", "ikw", "ikx", "iky", "ikz", "ik "]:
                x = "i`"
                x = x + last
            if x in ["ukb", "ukc", "ukd", "ukf", "ukg", "ukh", "ukj", "ukk", "ukl", "ukm", "ukn", 
                    "ukp", "ukq", "ukr", "uks", "ukt", "ukv", "ukw", "ukx", "uky", "ukz", "uk "]:
                x = "u`"
                x = x + last
            if x in ["ekb", "ekc", "ekd", "ekf", "ekg", "ekh", "ekj", "ekk", "ekl", "ekm", "ekn", 
                    "ekp", "ekq", "ekr", "eks", "ekt", "ekv", "ekw", "ekx", "eky", "ekz", "ek "]:
                x = "e`"
                x = x + last
            if x in ["okb", "okc", "okd", "okf", "okg", "okh", "okj", "okk", "okl", "okm", "okn", 
                    "okp", "okq", "okr", "oks", "okt", "okv", "okw", "okx", "oky", "okz", "ok "]:
                x = "o`"
                x = x + last
            semiout = semiout+x

    wordlist = list(semiout)
    wordlist.append(" ")
    first = wordlist[0]
    semiout = ""
    for x in range(len(wordlist)): #*second loop
        if x%3 == 1:
            last = wordlist[x+2]
            x = wordlist[x]+wordlist[x+1]+wordlist[x+2]
            if x in ["akb", "akc", "akd", "akf", "akg", "akh", "akj", "akk", "akl", "akm", "akn", 
                    "akp", "akq", "akr", "aks", "akt", "akv", "akw", "akx", "aky", "akz", "ak "]:
                x = "a`"
                x = x + last
            if x in ["ikb", "ikc", "ikd", "ikf", "ikg", "ikh", "ikj", "ikk", "ikl", "ikm", "ikn", 
                    "ikp", "ikq", "ikr", "iks", "ikt", "ikv", "ikw", "ikx", "iky", "ikz", "ik "]:
                x = "i`"
                x = x + last
            if x in ["ukb", "ukc", "ukd", "ukf", "ukg", "ukh", "ukj", "ukk", "ukl", "ukm", "ukn", 
                    "ukp", "ukq", "ukr", "uks", "ukt", "ukv", "ukw", "ukx", "uky", "ukz", "uk "]:
                x = "u`"
                x = x + last
            if x in ["ekb", "ekc", "ekd", "ekf", "ekg", "ekh", "ekj", "ekk", "ekl", "ekm", "ekn", 
                    "ekp", "ekq", "ekr", "eks", "ekt", "ekv", "ekw", "ekx", "eky", "ekz", "ek "]:
                x = "e`"
                x = x + last
            if x in ["okb", "okc", "okd", "okf", "okg", "okh", "okj", "okk", "okl", "okm", "okn", 
                    "okp", "okq", "okr", "oks", "okt", "okv", "okw", "okx", "oky", "okz", "ok "]:
                x = "o`"
                x = x + last
            semiout = semiout + x
    semiout = first + semiout

    wordlist = list(semiout)
    wordlist.append(" ")
    firstsec = wordlist[0] + wordlist[1]
    for x in range(len(wordlist)): #*third loop
        if x%3 == 2:
            last = wordlist[x+2]
            x = wordlist[x]+wordlist[x+1]+wordlist[x+2]
            if x in ["akb", "akc", "akd", "akf", "akg", "akh", "akj", "akk", "akl", "akm", "akn", 
                    "akp", "akq", "akr", "aks", "akt", "akv", "akw", "akx", "aky", "akz", "ak "]:
                x = "a`"
                x = x + last
            if x in ["ikb", "ikc", "ikd", "ikf", "ikg", "ikh", "ikj", "ikk", "ikl", "ikm", "ikn", 
                    "ikp", "ikq", "ikr", "iks", "ikt", "ikv", "ikw", "ikx", "iky", "ikz", "ik "]:
                x = "i`"
                x = x + last
            if x in ["ukb", "ukc", "ukd", "ukf", "ukg", "ukh", "ukj", "ukk", "ukl", "ukm", "ukn", 
                    "ukp", "ukq", "ukr", "uks", "ukt", "ukv", "ukw", "ukx", "uky", "ukz", "uk "]:
                x = "u`"
                x = x + last
            if x in ["ekb", "ekc", "ekd", "ekf", "ekg", "ekh", "ekj", "ekk", "ekl", "ekm", "ekn", 
                    "ekp", "ekq", "ekr", "eks", "ekt", "ekv", "ekw", "ekx", "eky", "ekz", "ek "]:
                x = "e`"
                x = x + last
            if x in ["okb", "okc", "okd", "okf", "okg", "okh", "okj", "okk", "okl", "okm", "okn", 
                    "okp", "okq", "okr", "oks", "okt", "okv", "okw", "okx", "oky", "okz", "ok "]:
                x = "o`"
                x = x + last
            out = out + x
    out = firstsec + out

    return out

def main():
    print("Masukkan kalimat yang ingin diganti")
    msg = input(">>>")
    msg = changesingleconsonant(msg)
    msg = changedoubleconsonant(msg)
    msg = changetripleconsonant(msg)
    print("\n \nOutput:")
    pyperclip.copy(msg)
    print(msg)
    print("text copied in clipboard")

main()
