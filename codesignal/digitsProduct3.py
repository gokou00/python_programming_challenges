import numpy
import itertools


def get_digits(arr,num):
    pop = 0
    
    while num != 0:
        pop = num % 10
        arr.append(pop)
        num = num //10
        
        

def digitsProduct(product):
    num_array = []
    if product == 0:
        return 10
    
    if product == 1:
        return 1
    
    for i in range(2,product):
        if product % i == 0:
            print(i)
            if i > 9:
                #get_digits(num_array,i)
                for j in range(2,i):
                    if i % j == 0:
                        if j > 9:
                            get_digits(num_array,j)
                        else:
                            
                            num_array.append(j)
            else:
                num_array.append(i)
    
    
    print(num_array)
    count = 0
    num_array2 =[]
    
    for i in num_array:
        if i == 0:
            continue
        elif i == 1:
            continue
        num_array2.append(i)
        
            
            
    print(num_array2)
    
    product_array = []
    all_com = []
    
    #stuff = [1, 2, 3]
    for L in range(0, 5):
        for subset in itertools.combinations(num_array2, L):
            #print(list(subset))
            #all_com.append(list(subset))
            if numpy.prod(list(subset)) == product:
                all_com.append(list(subset))
                break
    
    print(all_com)
    
    if len(all_com) == 0:
        return -1
        
    final_array = all_com[0]
    
    final_array.sort()
    
    finalstr = ""
    
    for x in final_array:
        finalstr += str(x)
    
    return int(finalstr)
    
    #for x in all_com:
        #if numpy.prod(x) == product:
            #product_array.append(x)
    #print(product_array)

print(digitsProduct(578))
    
    
    
    
    
    

    