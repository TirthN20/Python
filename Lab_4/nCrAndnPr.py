def fact(n):
    b=1
    for i in range(1,n+1) :
        b=b*i
    return b
def nCr(n,r):
    t=(fact(n))/(fact(r)*fact(n-r))
    print("nCr : ",t)
def nPr(n,r):
    z=(fact(n))/(fact(n-r))
    print("nPr : ",z)



a=int(input("Enter n : "))
q=int(input("Enter r : "))

nCr(a,q)
nPr(a,q)
