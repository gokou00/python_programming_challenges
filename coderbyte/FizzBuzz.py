def FizzBuzz(num):
    ansStr = ""
    for i in range(1,num+1):
        if i % 15 == 0:
            ansStr += "FizzBuzz "
        elif i % 5 == 0:
            ansStr += "Buzz "
        elif i % 3 == 0:
            ansStr += "Fizz "
        else:
            ansStr+= str(i)
            ansStr+= " "
    
    return ansStr
    
print(FizzBuzz(3))