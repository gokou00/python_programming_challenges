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
    
    for i in range(2,product):
        if product % i == 0:
            if i > 9:
                get_digits(num_array,i)
            else:
                num_array.append(i)
    
    
    print(num_array)
    
    product_array = []
    
    subs = [[]]
    for i in range(len(num_array)):
        n = i+1
        while n <= len(num_array):
            sub = num_array[i:n]
            subs.append(sub)
            n += 1
    
    print(subs)
    
    for x in subs:
        if numpy.prod(x) == product:
            product_array.append(x)
    
    stuff = [1, 2, 3]
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            print(list(subset))
    
    print(product_array)

digitsProduct(12)
    
    
    
    
    
    

    