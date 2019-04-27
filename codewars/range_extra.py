def solution(args):
    # your code here
    finalStr = ""
    args.sort()
    #print(args)
    #finalStr += str(args[0]) + ","
    #print(args[len(args) -1])
    last = args[len(args) -1]
    iscontin = False
    
    for i in range(args[0],last + 1):
        if i == args[0]:
            finalStr += str(args[0])
            continue
        if i not in args and finalStr[len(str)-1] != ",":
            finalStr += ","
            continue
        if i not in args:
            continue
        
        if i in args:
            finalStr += str(i)
            finalStr += "-"
            iscontin = True
            
        
        
        

    
    #print(finalStr)
    
    
solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
            