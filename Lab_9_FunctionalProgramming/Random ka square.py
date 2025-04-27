import random
l=[]
for i in range(0,10):
    l.append(random.randint(-15,15))
print(l)
m=list(map(lambda n:n**2,l))
print(m)
    
