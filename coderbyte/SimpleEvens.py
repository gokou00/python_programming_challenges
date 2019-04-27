def SimpleEvens(num):
    while num != 0:
        pop = num % 10
        if pop % 2 != 0:
            return "false"
        num /= 10
    
    return "true"


print(SimpleEvens(4602225))