import math
#http://virtualnerd.com/middle-math/integers-coordinate-plane/coordinate-plane/calculate-area-rectangle-vertices

def RectangleArea(strArr):
    coor1 = strArr[0]
    coor2 = strArr[1]
    coor3 = strArr[2]
    coor4 = strArr[3]
    width = 0
    length = 0
    
    
    #x1 = int(coor1[1])
    #x2 = int(coor2[1])
    #y1 = int(coor1[3])
    #y2 = int(coor2[3])
    
    indx = coor1.index(" ")
    
    x1 = int(coor1[1:indx])
    y1 = int(coor1[indx+1:len(coor1)-1])
    
    indx = coor2.index(" ")
    
    if y1 == int(coor2[indx+1:len(coor2)-1]):
        x2 = int(coor2[1:indx])
        y2 = int(coor2[indx+1:len(coor2)-1])
        width = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
        
    indx = coor3.index(" ")
    if y1 == int(coor3[indx+1:len(coor3)-1]):
        x2 = int(coor3[1:indx])
        y2 = int(coor3[indx+1:len(coor3)-1])
        width = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
    
    indx = coor4.index(" ")
    
    if y1 == int(coor4[indx+1:len(coor4)-1]):
        x2 = int(coor4[1:indx])
        y2 = int(coor4[indx+1:len(coor4)-1])
        width = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
        
    indx = coor2.index(" ")
    if x1 == int(coor2[1:indx]):
        x2 = int(coor2[1:indx])
        y2 = int(coor2[indx+1:len(coor2)-1])
        length = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
    
    indx = coor3.index(" ")
    if x1 == int(coor3[1:indx]):
        x2 = int(coor3[1:indx])
        y2 = int(coor3[indx+1:len(coor3)-1])
        length = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
        
    indx = coor4.index(" ")
    if x1 == int(coor4[1:indx]):
        x2 = int(coor4[1:indx])
        y2 = int(coor4[indx+1:len(coor4)-1])
        length = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))

    return int(width * length)
    


    
    
print(RectangleArea(["(1 1)","(4 4)","(1 4)","(4 1)"]))