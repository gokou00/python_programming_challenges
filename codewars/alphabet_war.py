def alphabet_war(fight):
    print(fight)
    
    dic = {}
    dic["w"] = 4
    dic["p"] = 3
    dic["b"] = 2
    dic["s"] = 1
    dic["m"] = 4
    dic["q"] = 3
    dic["d"] = 2
    dic["z"] = 1
    left_side = 0
    right_side = 0
    left_arr = "wpbs"
    right_arr = "mqdz"
    fights = list(fight)
    strArry = []
    fight2 = ""
    

            
            
    while "**" in fight:
        index = fight.index("**")
        temp = list(fight)
        del temp[index]
        fight = "".join(temp)
    
    
    print(fight, "test")
            
            
        

    
    strArry2 = list(fight)
    
    while "*" in strArry2:
        index = strArry2.index("*")
        
        if len(strArry2) == 0:
            return "Let's fight again!"
        #if index -1 < 0 or index + 1 > len(strArry2) -1:
            #continue
        
        if index -1 >= 0:
            strArry2[index-1] = "_"
        
        if index + 1 <= len(strArry2) -1:
            strArry2[index+1] = "_"
        
        #strArry2[index+1] = "_"
        #strArry2[index-1] = "_"
        strArry2[index] = "_"
    
 
        
    
    print(strArry2)    
    
    fight = "".join(strArry2)
    print(fight)
    
        
        
    
        
    
    
    for x in fight:
        if x in left_arr:
            left_side += dic[x]
        if x in right_arr:
            right_side += dic[x]
        else:
            continue
    if left_side > right_side:
        return "Left side wins!"
    if right_side > left_side:
        return "Right side wins!"
    
    return "Let's fight again!"
    
print(alphabet_war("mb**qwwp**dm"))