def RunLength(string):
    stringarr = []
    
    final_str = ""
    
    for x in string:
        if x in stringarr:
            stringarr.append(x)
        elif x not in stringarr and len(stringarr) !=0:
            final_str += str(len(stringarr))
            final_str += stringarr[0]
            stringarr = []
            stringarr.append(x)
        else:
            stringarr.append(x)
    
    if len(stringarr) != 0:
        final_str += str(len(stringarr))
        final_str += stringarr[0]
    
    print(final_str)


print(RunLength("mouses"))
        