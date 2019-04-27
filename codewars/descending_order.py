def Descending_Order(num):
    #Bust a move right here
    print(num)
    numStr = str(num)
    print(numStr)
    if num == 0 or num == None:
        return 0
    
    num_array = list(numStr)
    print(num_array)
    
    for i in range(len(num_array)):
        num_array[i] = int(num_array[i])
        
    
    print(num_array)
    
    num_array.sort(reverse = True )
    for i in range(len(num_array)):
        num_array[i] = str(num_array[i])
    print(num_array)
    
    test = "".join(num_array)
    
    print(test)
    
        
    
    
Descending_Order(15)