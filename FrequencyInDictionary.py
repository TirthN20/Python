a=input("Enter a sentence : ")
dict1={}
dict2={}
for i in a :
    frequency=a.count(i)
    dict1={i:frequency}
    dict2={**dict2,**dict1}
print(dict2)
