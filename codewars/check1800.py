import re
def check1800(s):
    # Your code here!
    regexbuilder1 = ""
    regexbuilder2 = ""
    phonedict = {}
    phonedict[""] #create a dict with each letter in alpha as keys and values = to the keypad mappings. 
    
    r = re.compile("[WXYZ]{1}[ABC]{1}[PQRS]{1}")
    newlist = list(filter(r.match, WORDS))
    print(newlist)
    #build both list based on the re and length of the words. 
    pass