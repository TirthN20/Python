def san(l,l1,i):
    if i==(len(l)):
        return l1
    else:
        if l[i]>=0:
            l1.append(l[i])
        else :
            l1.append(0)
        return san(l,l1,i+1)



l=[1,2,3,-1,-2,-3,0]
l1=[]
print(san(l,l1,0))
