t=(1,3,5,4,2,43)
print(t)
t2=()
a=int(input("Enter the element to be modified : "))
n=int(input("Enter the new element : "))
for i in t :
    if i==a :
        t2=t2 + (n,)
    else :
        t2=t2 + (i,)
print("The modified tuple is : ") 
print(t2)
    
