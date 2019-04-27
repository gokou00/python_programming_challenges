def josephus_survivor(n,k):
    #your code here
    que = []
    for i in range(1,n+1):
        que.insert(0,i)
    
    #print(que)
    
    while len(que) > 1:
        #print(que)
        for _ in range(k-1):
            temp = que.pop()
            que.insert(0,temp)
            #print("t")
            
        que.pop()
        
    if(len(que) == 1):
        return que.pop()
    if(len(que) == 0):
        return []
    if(len(que) > 1):
        return que.pop(0)
        
print(josephus_survivor(10,3))
    