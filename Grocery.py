G1={'Mung':120,'banana':5}
G2={'Mung':2,'banana':12}
l1=[]
l2=[]
for v in G1.values():
    l1.append(v)
for v in G2.values():
    l2.append(v)
print(l1)
print(l2)
total=l1[0]*l2[0] + l1[1]*l2[1]
print(total)
    
    
