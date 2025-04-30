f=open("C:\\Users\\Tirth\\OneDrive\\Desktop\\Book1.csv",'r')
d={}
l=[]
l1=f.readlines()
print(l1)
for i in l1:
    l.append(i.strip().split(","))
print(l)
for i in range(len(l[0])):
    d[l[0][i]]=[l[1][i],l[2][i],l[3][i]]
print(d)
f.close()
    
