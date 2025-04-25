t=(1,2,3,4,5,10)
print(t)
l1=list(t)
a=int(input("Enter element to be removed : "))
for i in l1 :
      if (i==a) :
        l1.remove(i)
t2=tuple(l1)
print(t2)
      
