l=['madam','Python',"malayalam",12321]
def isPal(s):
    s2=''
    if type(s)==str:
        for i in range(len(s)-1,-1,-1):
            s2=s2+s[i]
        if s2==s:
            return True
        else :
            return False
    else :
        return False
        
f=list(filter(isPal,l))
print(f)

        
    
