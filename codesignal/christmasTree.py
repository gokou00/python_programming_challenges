def christmasTree(levelNum, levelHeight):
    count = levelHeight * 2 + 3
    
    if levelNum > 1:
        for i in range(levelNum-1):
            count +=  2
            
        
    
    print(count)
    tree = []
    tree.append("      *")
    tree.append("      *")
    tree.append("     ***")
    lvl = "     ***"
    
    for i in range(levelHeight):
        lvlArr = list(lvl)
        lvlArr.append("*")
        idx = lvlArr.index("*")
        lvlArr[idx-1] = "*"
        lvl = "".join(lvlArr)
        tree.append(lvl)
    
    
    print(tree)



print(christmasTree(4,8))
    
    