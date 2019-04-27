def isMatch(s, p):
    if "*" not in p and len(s) != len(p):
        return False
    
    
    