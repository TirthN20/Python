s1=set()
s2=set()
s=set()
while len(s)<4 :
    a=input("Enter name starting with A or B : ")
    for i in range(0,10) :
        if a[i]=='A' :
            s1.add(a)
            s.add(a)
        elif a[i]=='B' :
            s2.add(a)
            s.add(a)
print(s)
print(s1)
print(s2)
            
            

    
    
