def los(s,count,i):
    if s=='':
        return count
    else :
        count+=1
        return los(s[1:],count,i)



s='tirth'
print(los(s,0,0))
