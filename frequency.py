def frequency(a):
    b=sorted(a.split())
    print(b)
    l=[]
    dict={}
    for i in b :
        if i not in l:
            l.append(i)
            c=b.count(i)
            dict.update({i:c})
    print(dict)




a=input("Enter a string : ")
frequency(a)
