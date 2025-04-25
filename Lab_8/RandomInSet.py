import random
s=set()
count=0
while len(s)<10 :
    for i in range(0,1) :
        x=random.randint(15,45)
        s.add(x)
print(s)

for i in s :
    if i<30 :
        count+=1

print("Elements less than 30 are : ",count)

for i in list(s) :
    if i>35 :
        s.remove(i)
set(s)
print("Modified set : ",s)

"""for i in s :
    if i<35 :
        s2.add(i)"""




        
