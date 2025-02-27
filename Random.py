import random
s=set()
s2=set()
count=0
while len(s)<10 :
    for i in range(0,1) :
        a=random.randint(15,45)
        s.add(a)
        
print(s)

for i in s :
    if i<30 :
        count=count+1

for i in s :
    if i<35 :
        s2.add(i)
        
print(s2)
print("The numbers less than 30 are : ",count)
