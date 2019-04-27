def BinaryReversal(string):
    return str(int('{0:08b}'.format(int(string))[::-1],2))
    #binary = 
    #revbin = binary[::-1]
    #print(int(revbin,2))
    
    #return 
    #print(binary)
    
    
print(BinaryReversal("47"))