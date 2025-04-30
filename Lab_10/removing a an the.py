f=open("C:\\Users\\Tirth\\OneDrive\\Desktop\\6.txt",'r')
f2=open("NewAfterA,an,the.txt",'w+')
x=f.read()
print(x)
w=x.split()
print(w)
r=['an','a','the','A','An','The']

new=[i for i in w if i not in r]
print(new)
add=' '.join(new)
f2.write(add)
f.close()
f2.close()

