def jumpingOnClouds(c):
    arrCount = 0
    jumpCount = 0
    
    while arrCount < len(c):
        if (arrCount + 2) < len(c):
            if c[arrCount+2] == 0:
                arrCount += 2
                jumpCount += 1
                continue
            else:
                arrCount += 1
                jumpCount += 1
                continue
        else:
            arrCount+=1
            jumpCount+=1
    
    
    return jumpCount -1 


print(jumpingOnClouds([0, 0, 0, 0 ,1 ,0]))
