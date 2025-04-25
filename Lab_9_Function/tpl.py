def tpl(n):
    l=[]
    for i in range(1,n+1):
        t=(i,i**2,i**3)
        l.append(t)
    print(l)



n=int(input("Enter a number :"))
tpl(n)
