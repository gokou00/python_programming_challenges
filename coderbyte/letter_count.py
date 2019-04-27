string = "Hello apple pie" 
test = {}
temp = 0 
#test["hello"] = []
#test["hello"].append(3)

str_array = string.split(" ")
print(str_array)

count = 0 

for word in str_array:
    test[word] = 0
    for letter in word:
        if word.count(letter) >= 2 and word.count(letter) > temp :
            test[word] = word.count(letter)
            temp = word.count(letter)
            count = temp
    
    temp = 0
        

print(str(count) + " temp")

if count == 0:
    return -1

temp = 0
answer = str_array[1]
for key,value in test.items():
    print(str_array.index(key))
    


for key,value in test.items():
    if value > temp:
        answer = key
        temp = value
    elif value == temp:
        if str_array.index(answer) < str_array.index(key):
            continue
        else:
            answer = key
        
    
    
return answer





#for x in string:
    


#print(test)

#for x in test:
    #print(test[x][0])
