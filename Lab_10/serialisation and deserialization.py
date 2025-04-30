import json
employee={'empcode':2,'empname':'xyz','Date of joining':'20/5/2006','Salary':'1000000'}
f=open("SandD.txt",'w+')
json.dump(employee,f)
f.seek(0)
d=json.load(f)
print(d)
f.close()
    
