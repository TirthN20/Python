f=open("C:\\Users\\Tirth\\OneDrive\\Desktop\\Book1.csv",'r')
a=f.read().upper()
f2=open("Newfile.csv",'w+')
f2.write(a)
f.close()
f2.close()

