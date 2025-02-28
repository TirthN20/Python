from datetime import date
t1=date(2006,9,30)
t2=date(2025,2,28)
a=0
if t1>t2 :
    a=(t1-t2).days
else :
    a=(t2-t1).days

print(a)


    
