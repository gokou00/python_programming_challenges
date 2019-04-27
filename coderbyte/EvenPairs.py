#import itertools

def EvenPairs(string):
    count = 0
    strbuild = ""
    strArry = []
    
    for x in string:
        if x >= "0" and x <= "9":
            strbuild += x
        elif len(strbuild) > 0:
            strArry.append(strbuild)
            strbuild = ""
    
    if len(strbuild) != 0:
        strArry.append(strbuild)
    
    for x in strArry:
        count = check(x)
        if count >=2:
            return "true"
    
    #print(strArry)
    #return "false"
    
    #strbuild = ""
    
    #test = "9846"
    #print(test[-4:len(test)])
       
    return "false"
    
def check(string):
    count = 0
    for i in range(len(string)):
        neg = (i +1) *-1
        if int(string[neg:len(string)]) % 2 == 0:
            count+=1
    
    return count            

print(EvenPairs("106a"))