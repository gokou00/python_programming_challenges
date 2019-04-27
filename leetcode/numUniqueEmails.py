def numUniqueEmails(emails):
    filteredArr = []
    strbuild = ""
    emaildict = {}
    
    for x in emails:
        idx = x.index("@")
        domain = x[idx:]
        x = x[:idx]
        for l in x:
            if l == ".":
                continue
            if l == "+":
                break
            strbuild += l
        
        temp = strbuild +domain
        filteredArr.append(temp)
        strbuild = ""
    
    #print(filteredArr)
    for x in filteredArr:
        emaildict[x] = 0
    
    #print(len(emaildict))
    return len(emaildict)
    


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))