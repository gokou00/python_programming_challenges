def addTwoNumbers(l1, l2):
        string1 = ""
        string2 = ""
        
        
        # this is for a link list 
        while l1 != None:
            string1 += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            string2 += str(l2.val)
            l2 = l2.next
        
        num1 = int(string1[::-1])
        #print(num1)
        num2 = int(string2[::-1])
        #print(num2)
        finalArr = []
        total = num1 + num2
        
        if total == 0:
            return[0]
        
        while total != 0:
            pop = total % 10
            finalArr.append(pop)
            total //= 10
        
        return finalArr