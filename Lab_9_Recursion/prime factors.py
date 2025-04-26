def pf(n,i=2):
    if(n==1):
        return 
    elif n%i==0:
        print(i)
        return pf(n//i,i)
    else :
        return pf(n,i+1)

n=int(input("Enter a number : "))
print(pf(n,i=2))
