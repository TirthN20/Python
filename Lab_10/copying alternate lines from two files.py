f1=open("C:\\Users\\Tirth\\OneDrive\\Desktop\\file 1.txt",'r')
f2=open("C:\\Users\\Tirth\\OneDrive\\Desktop\\file 2.txt",'r')
f3=open("file3.txt",'w+')
l1=f1.readlines()
l2=f2.readlines()
maxx=max(len(l1),len(l2))
print(maxx)
f1.seek(0)
f2.seek(0)
for i in range(maxx):
    x=f1.readline()
    f3.write(x)
    y=f2.readline()
    f3.write(y)
f1.close()
f2.close() 
f3.close()


