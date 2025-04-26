def avg(l,i,sum):
    if i==len(l):
        return (sum/len(l))
    else :
        sum=sum+l[i]
        return avg(l,i+1,sum)



l=[1,2,3,4,5]
print(avg(l,0,0))
