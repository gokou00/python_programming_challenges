
import re    
def alphanumericLess(s1, s2):
    if s1==s2:
        return False
    
    seq1 = ([i for i in re.split(r'(\d+|\D)', s1) if i])
    seq2 = ([i for i in re.split(r'(\d+|\D)', s2) if i])
    allEqual = True
    
    if len(seq1)>len(seq2):
        return False
    elif len(seq1)<len(seq2):
        return True
    
    for i in range(0,len(seq1)):
        if 'a'<=seq1[i]<='z':
            if seq1[i]>seq2[i]:
                return False
            elif seq1[i]<seq2[i]:
                allEqual = False
        else:
            if int(seq1[i])>int(seq2[i]):
                return False
            elif int(seq1[i])<int(seq2[i]):
                allEqual = False
    
    if allEqual:
        for i in range(0,len(seq1)):
            if 'a'<=seq1[i]<='z':
                pass
            else:
                if int(seq1[i])==int(seq2[i]):
                    if len(seq1[i])<len(seq2[i]):
                        return False
    return True
    