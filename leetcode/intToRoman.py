def intToRoman(num):
    #roman = {}
    #roman["M"] = 1000
    romanAns = ""
    
    total = num // 1000
    romanAns += "M" * total
    num %= 1000
    
    total = num // 900
    romanAns += "CM" * total
    num %= 900
    
    
    
    
    total = num // 500
    romanAns += "D" * total
    num %= 500
    
    total = num // 400
    romanAns += "CD" * total
    num %= 400
    
    
    
    
    total = num // 100
    romanAns += "C" * total
    num %= 100
    
    total = num // 90
    romanAns += "XC" * total
    num %= 90
    
    
    total = num // 50
    romanAns += "L" * total
    num %= 50
    
    total = num // 40
    romanAns += "XL" * total
    num %= 40
    
    
    
    total = num // 10
    romanAns += "X" * total
    num %= 10
    
    total = num // 9
    romanAns += "IX" * total
    num %= 9
    
    
    
    
    
    total = num // 5
    romanAns += "V" * total
    num %= 5
    
    
    total = num // 4
    romanAns += "IV" * total
    num %= 4
    
    
    
    
    total = num // 1
    romanAns += "I" * total
    num %= 1
    
    
    return romanAns
    
print(intToRoman(9))
    
    
    