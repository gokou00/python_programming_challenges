def characterParity(symbol):
    if symbol >= "0" and symbol <= "9":
        num = int(symbol)
    else:
        return "not a digit"
        
    
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


