def repeatedString(s, n):
    countA = 0
    buildStr = ""
    if len(s) > n:
        for i in range(n):
            buildStr += s[i]
        
        return buildStr.count("a")
    else:
        #buildStr += s * (n//len(s))
        buildStr += s * (1000000000000)
        leftover = n % len(s)
        for i in range(leftover):
            buildStr += s[i]
        return buildStr.count("a")




print(repeatedString("a",1000000000000))
        