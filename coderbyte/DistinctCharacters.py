def DistinctCharacters(string):
    dist = {}
    for x in string:
        dist[x] = 0
    
    if len(dist) >= 10:
        return "true"
    else:
        return "false"


print(DistinctCharacters("eeeemmmmmmmmm1000"))
