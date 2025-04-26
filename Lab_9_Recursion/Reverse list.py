def rev(l,l1,i):
    if i==-1:
        return l1
    else :
        l1.append(l[i])
        return rev(l,l1,i-1)

l=[1,2,3,4,5]
l1=[]
print(rev(l,l1,len(l)-1))
