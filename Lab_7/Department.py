d={(1,1):10000,(1,2):20000,(1,3):30000,(2,10):50000,(2,20):75000,(2,30):100000}
mm={}
for k,v in d.items() :
    print(k[0],k[1],v)

    if k[0] not in mm :
        mm[k[0]]=[v]
    else :
        mm[k[0]].append(v)

print(mm)

for key in mm :
    mm[key]={'Max':max(mm[key]),'Min':min(mm[key]),'Total':sum(mm[key])}
print(mm)
    
    
