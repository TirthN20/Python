s=set()
while len(s)<5 :
    for i in range(0,1) :
        s.add(input("Enter name : "))

print(s)

a=input("Enter the element to be modified : ")

if a in s :
    b=input("Enter the new element : ")
    s.remove(a)
    s.add(b)
    
else :
    print("Enter the element present in set ")

print(s)

e=input("Enter first element to be removed : ")
f=input("Enter second element to be removed : ")

s.remove(e)
s.remove(f)

print("The modified set is : ",s)




        
