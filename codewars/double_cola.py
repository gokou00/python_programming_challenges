def whoIsNext(names, r):
    # your code
    queue_list = []
    name = ""
    
    for x in names:
        queue_list.insert(0,x)
        
    if(r == 1):
        return queue_list.pop()    
    
    
    for i in range(r):
        name = queue_list.pop()
        queue_list.insert(0,name)
        
    return queue_list.pop()
    
        

print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951))