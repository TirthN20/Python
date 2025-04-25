#Create two dictionaries – one containing grocery items and their prices and
#another containing grocery items and quantity purchased.
#By using the values from these two dictionaries compute the total bill.


G1={'Mung':120,'banana':5}
G2={'Mung':2,'banana':12}
l1=[]
l2=[]

for i in G1.values() :
    l1.append(i)
for i in G2.values():
    l2.append(i)
x=0
for i in range(0,len(l1)):
    x=x+l1[i]*l2[i]

print(x)
