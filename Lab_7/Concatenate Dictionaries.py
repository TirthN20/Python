"""d = {72: 'Darshit' , 60: 'Amita' , 58 : 'Ashit' , 52: 'Parul', 54 : 'Devang', 56 : 'Nina'}
n = { 74: 'Ragi', 2006 : 'Aashna' }
t={1:20,2:26,3:27}
s={**d,**n,**t}
print(s)"""
a={}
q=int(input("Enter the number of pairs : "))
for i in range(0,q) :
    key=(input("Enter key : "))
    value=(input("Enter value : "))
    a.update({key:value})

print(a)
