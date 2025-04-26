def vo(s,count,i):
    l=['a','e','i','o','u','A','E','I','O','U']
    if i==len(s):
        return count
    elif (s[i] in l):
        count+=1
        return vo(s,count,i+1)
    else:
        return vo(s,count,i+1)
    
s=input("Enter a string : ")
print(vo(s,0,0))
