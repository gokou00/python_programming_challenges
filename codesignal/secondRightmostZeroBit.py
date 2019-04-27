def secondRightmostZeroBit(n):
    #return bin(n)[2:][::-1].index("0")
    #return bin(n)[2:][::-1][2:].index("0")
    return  ~(n|n+1) & -~(n|n+1)  
    

print(secondRightmostZeroBit(37))