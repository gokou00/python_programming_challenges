def higherVersion(ver1, ver2):
    if "." not in ver1 and ver2:
        if int(ver1) > int(ver2):
            return True
        else:
            return False
    
    
    ver1Str = ""
    ver2Str = ""
    
    ver1Arr = ver1.split(".")
    ver2Arr = ver2.split(".")
    
    
    for i in range(len(ver1Arr)):
        if int(ver1Arr[i]) == int(ver2Arr[i]):
            continue
        elif int(ver1Arr[i]) > int(ver2Arr[i]):
            return True
            
        elif int(ver1Arr[i]) < int(ver2Arr[i]):
            return False
    
    
    for x in ver1:
        if x == ".":
            continue
        ver1Str += x
    
    
    for x in ver2:
        if x == ".":
            continue
        ver2Str += x
    
    
    if int(ver1Str) > int(ver2Str):
        return True
    else:
        return False
        
    
    

    
    

print(higherVersion("4.3.22.1","4.3.22.1"))
            
    