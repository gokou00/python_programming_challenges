def checkRecord(s):
    late =  s.count("LLL")
    Absent = s.count("A")
    
    if late > 0 or Absent > 1:
        return False
    else:
        return True
    



print(checkRecord("PPALLP"))
