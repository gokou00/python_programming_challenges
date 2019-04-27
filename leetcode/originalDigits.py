#could creat a dict of char nums compare with each word in the arr
from collections import Counter

def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    #test = letters - word
    #print(test)
    diff = word - letters
    #print(diff)
    
    #buildStr = ""
    #for x in test:
        #buildStr+= x*test[x]
    
    
    return (len(diff) == 0) 
    


def buildNewStr(c):
    buildStr = ""
    for x in c:
        buildStr+= x*c[x]
    return buildStr

def originalDigits(s):
    count = 0
    numDigts = 0
    finalStr = ""
    digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for (i,x) in enumerate(digits):
        if scramble(s,x):
            s1 = Counter(s)
            s2 = Counter(x)
            temp = s1 - s2
            s = buildNewStr(temp)
            finalStr += str(i)
    
            
    if len(s) > 0:
        for x in digits:
        #print(x)
        #test,temp = scramble(s,x)
            while(scramble(s,x)):
            #print(temp)
            #s = temp
                s1 = Counter(s)
                s2 = Counter(x)
                temp = s1 - s2
            
                s = buildNewStr(temp)
            
                numDigts+=1
            #test,s = scramble(s,x)
        
            if numDigts >0:
                finalStr += str(count)*numDigts
        
            numDigts = 0
            count+=1
        
    
    
    
    
    
    if numDigts >0:
        finalStr += str(count)*numDigts
            
    return finalStr
    #print(scramble(s,"one"))
    
    
print(originalDigits("fviefuro"   ))
    
    
    

    