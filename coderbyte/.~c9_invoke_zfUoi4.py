import math

def RectangleArea(strArr):
    coor1 = strArr[0]
    coor2 = strArr[1]
    coor3 = strArr[2]
    
    
    
    #x1 = int(coor1[1])
    #x2 = int(coor2[1])
    #y1 = int(coor1[3])
    #y2 = int(coor2[3])
    
    indx = coor1.index(" ")
    
    x1 = int(coor1[1:indx])
    x2 = int(coor1[indx+1:])
    
    
    
    

    
    #print(int("-"))
    
    #width = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
    #print(width)
    
    #x2 = int(coor3[1])
    #y2 = int(coor3[3])
    
    #length = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
    
    #print(length)
    
    #return int(width * length)
    
    
print(RectangleArea(["(-122 0)","(1 0)","(1 1)","(0 1)"]))