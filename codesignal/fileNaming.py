from collections import OrderedDict
def fileNaming(names):
    file = OrderedDict()
    arr = []
    
    for x in names:
        if x not in file:
            file[x] = 0
            arr.append(x)
        else:
            file[x] +=1
            temp = x
            temp += "("
            temp += str(file[x])
            temp += ")"
            while(temp in file):
                file[x]+=1
                temp = x
                temp += "("
                temp += str(file[x])
                temp += ")"
                
            file[temp] = 0  
            arr.append(temp)
            
            
            
            

    
 
    return arr


print(fileNaming(["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]  ))
    
    
    