def NumberEncoding(string):
    alphaDict = {}
    alphaDict["a"] = 1
    alphaDict["b"] = 2
    alphaDict["c"] = 3
    alphaDict["d"] = 4
    alphaDict["e"] = 5
    alphaDict["f"] = 6
    alphaDict["g"] = 7
    alphaDict["h"] = 8
    alphaDict["i"] = 9
    alphaDict["j"] = 10
    alphaDict["k"] = 11
    alphaDict["l"] = 12
    alphaDict["m"] = 13
    alphaDict["n"] = 14
    alphaDict["o"] = 15
    alphaDict["p"] = 16
    alphaDict["q"] = 17
    alphaDict["r"] = 18
    alphaDict["s"] = 19
    alphaDict["t"] = 20
    alphaDict["u"] = 21
    alphaDict["v"] = 22
    alphaDict["w"] = 23
    alphaDict["x"] = 24
    alphaDict["y"] = 25
    alphaDict["z"] = 26
    
    strbuild = ""
    
    for x in string:
        if x.isalpha():
            strbuild += str(alphaDict[x])
        else:
            strbuild +=x
            
    
    return strbuild



print(NumberEncoding("jaj-a" ))
    
    