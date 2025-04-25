s=set()
s1=set()
s2=set()

while len(s)<4:
    for i in range(0,1):
        x=input("Enter a name starting with 'A' or 'B' : ")
        if (x[0]=='A' or x[0]=='B') :
            s.add(x)

for i in s :
    if i[0]=='A' :
        s1.add(i)
    else :
        s2.add(i)

print("Set with elements starting with 'A' : ",s1)
print("Set with elements starting with 'B' : ",s2)



