f=open("C:\\Users\\Tirth\\OneDrive\\Desktop\\Book1.csv",'r')
a=f.read()
f.close()
f2=open("New.csv",'w+')
f2.write(a)
f2.close()

#import shutil
#source="C:\\Users\\Tirth\\OneDrive\\Desktop\\Book1.csv"
#destination="new.txt"
#shutil.copy(source,destination)
