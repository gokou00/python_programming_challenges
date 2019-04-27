def solution(string,markers):
    finalStr = ""
    skip = False
    
    for x in string:
        if x.isalnum() == False and x in markers:
            skip = True
            continue
        elif x.isalnum() == False and x not in markers and x != " ":
            finalStr += x
            skip = False
        elif skip:
            continue
        else:
            finalStr += x
    
    print(finalStr)
    
solution("a #b\nc\nd $e f g", ["#", "$"])