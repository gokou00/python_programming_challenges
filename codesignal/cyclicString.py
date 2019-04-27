from collections import OrderedDict
def cyclicString(s):
    od = OrderedDict()
    for x in s:
        od[x] = 1
    
    
    newStr = ""
    
    for x in od.keys():
        newStr += x
    
    print(newStr)
    
    count = 0
    
    for x in range(len(s)):
        if s in newStr:
            break
        count += 1
        newStr += newStr
    
    return len(newStr)




print(cyclicString("bcaba"))
    